#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NGP(C) SNK 그림 아이템(타이틀 로고 등) ↔ PNG.  롬은 읽기만; 쓰기는 사본에만.

아이템 문법 (SS2 로고 0x0837B3 · 월화 로고 0x088200 에서 확인):
    cnt16 | ptr32(타일 기준, CPU 주소 = 파일+0x200000) | off16×cnt | 헤더 1B | 행 × [칸 × (타일, 팔레트바이트)] + ff ff
    팔레트바이트 = (팔레트 − pal_base)×2 | 비트7 좌우반전 | 비트6 상하반전.   타일 = 문자RAM 색인 − tile_base
    tile_base·pal_base 는 아이템 안에 없다(호출자 값). SS2: 128/4, 월화: 16/0.
    타일 16 B: 행 워드 LE(둘째 바이트 = 왼쪽 4px), 2bpp. 값 0 = 투명(배경).
    팔레트 표: 16개 × 4색 × 2B, 워드 = b<<8 | g<<4 | r (4비트씩).

프로파일(JSON): {"item":"0837B3","bank":"083DC9","bank_end":"084DE9","pal_tbl":"059188","pal_base":4,"cols":20,"rows":11}
    bank/bank_end = 타일을 새로 쓸 자리(없으면 ptr 기준부터). cols/rows 는 extract 가 지도에서 읽으니 확인용.

사용:
    extract <rom> <profile.json> <out.png> [scale]
    build   <rom_in> <profile.json> <in.png> <rom_out> [grow_cnt]
            PNG(cols*8 × rows*8, 팔레트 표에 있는 색만, 8×8 칸당 팔레트 하나) → 아이템 재조립.
            grow_cnt 를 주면 cnt 를 그만큼까지 키운다(뒤 자리 — 예: 영어 아이템 — 를 먹는다).
"""
import sys, json, struct, zlib

def read_png(path):
    d = open(path, "rb").read(); assert d[:8] == b"\x89PNG\r\n\x1a\n"
    pos = 8; idat = b""; w = h = ct = 0
    while pos < len(d):
        n = struct.unpack(">I", d[pos:pos+4])[0]; t = d[pos+4:pos+8]; body = d[pos+8:pos+8+n]; pos += 12 + n
        if t == b"IHDR": w, h, bd, ct = struct.unpack(">IIBB", body[:10]); assert bd == 8 and ct in (2, 6), "8비트 RGB/RGBA 만"
        elif t == b"IDAT": idat += body
    raw = zlib.decompress(idat); bpp = 3 if ct == 2 else 4; stride = w * bpp
    rows = []; prev = bytearray(stride); p = 0
    for y in range(h):
        f = raw[p]; line = bytearray(raw[p+1:p+1+stride]); p += 1 + stride
        for i in range(stride):
            a = line[i-bpp] if i >= bpp else 0; b = prev[i]; c = prev[i-bpp] if i >= bpp else 0
            if f == 1: line[i] = (line[i] + a) & 255
            elif f == 2: line[i] = (line[i] + b) & 255
            elif f == 3: line[i] = (line[i] + (a + b) // 2) & 255
            elif f == 4:
                pp = a + b - c; pa, pb, pc = abs(pp - a), abs(pp - b), abs(pp - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append([tuple(line[x*bpp:x*bpp+3]) for x in range(w)]); prev = line
    return w, h, rows

def write_png(rows, dst, scale=1):
    h = len(rows); w = len(rows[0]); Wd, Hd = w*scale, h*scale; raw = bytearray()
    for y in range(Hd):
        raw.append(0); r = rows[y//scale]
        for x in range(Wd): raw += bytes(r[x//scale])
    def ch(t, dd):
        c = t + dd; return struct.pack(">I", len(dd)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)
    open(dst, "wb").write(b"\x89PNG\r\n\x1a\n" + ch(b"IHDR", struct.pack(">IIBBBBB", Wd, Hd, 8, 2, 0, 0, 0)) + ch(b"IDAT", zlib.compress(bytes(raw), 9)) + ch(b"IEND", b""))

def load_profile(path):
    p = json.load(open(path))
    for k in ("item", "bank", "bank_end", "pal_tbl", "grow_limit"):
        if k in p and isinstance(p[k], str): p[k] = int(p[k], 16)
    p.setdefault("pal_base", 0)
    return p

def palettes(rom, tbl, P=None):
    # 롬 표(pal_tbl)가 없으면 프로파일 "pal_dump"(SP 코어 !vram 의 .pal, 오프셋 pal_dump_off: 스크롤1=0x80, 스크롤2=0x100)에서 읽는다
    src = rom; base = tbl
    if P and P.get("pal_dump"):
        src = open(P["pal_dump"], "rb").read(); base = int(P.get("pal_dump_off", "80"), 16)
    out = []
    for i in range(16):
        cols = []
        for c in range(4):
            w = src[base + 8*i + 2*c] | (src[base + 8*i + 2*c + 1] << 8)
            cols.append(((w & 0xF)*17, ((w >> 4) & 0xF)*17, ((w >> 8) & 0xF)*17))
        out.append(cols)
    return out

def parse_item(rom, a):
    cnt = rom[a] | (rom[a+1] << 8); ptr = int.from_bytes(rom[a+2:a+6], "little")
    offs = [rom[a+6+2*i] | (rom[a+7+2*i] << 8) for i in range(cnt)]
    q = a + 6 + 2*cnt; hdr = rom[q]; pos = q + 1; rows = []
    while True:
        row = []
        while rom[pos:pos+2] != b"\xff\xff":
            row.append((rom[pos], rom[pos+1])); pos += 2
            if len(row) > 64: raise SystemExit("행 끝 ff ff 를 못 찾음 @%06X — 아이템 머리가 틀렸다" % a)
        pos += 2; rows.append(row)
        # 다음 두 바이트가 (타일, 팔레트) 꼴이면 계속. 행 폭이 첫 행과 같을 때만 행으로 본다
        if len(rows) >= 64 or pos + 2 > len(rom): break
        nxt = rom[pos:pos+2*len(rows[0])+2]
        if len(nxt) < 2*len(rows[0])+2 or nxt[2*len(rows[0]):2*len(rows[0])+2] != b"\xff\xff": break
    return dict(start=a, cnt=cnt, ptr=ptr, offs=offs, hdr=hdr, rows=rows, map_start=q, end=pos)

def swap2(v):
    # 2bpp 픽셀 값의 비트 쌍은 «낮은 비트가 먼저»다: 하드웨어 값 = bit(14-2x)<<1 | bit(15-2x).
    # 값 0·3 은 대칭이라 글자(먹=1/3)만 다루던 도구들은 몰랐고, 팔레트 색 1·2 를 쓰는 로고에서 색이 뒤바뀌어 들통났다(월화 시제품).
    return v   # 화면 실측(월화 bits.ngc): 워드 0x55AA → 왼쪽 4px = 색1, 오른쪽 = 색2. 즉 비트 쌍은 MSB 먼저, 교환 없음

def tile_px(rom, off):
    return [[swap2((rom[off+2*y] | (rom[off+2*y+1] << 8)) >> (14 - 2*x) & 3) for x in range(8)] for y in range(8)]

def extract(rom, P, out, scale):
    it = parse_item(rom, P["item"]); pals = palettes(rom, P.get("pal_tbl"), P); base = it["ptr"] - 0x200000
    H = len(it["rows"]); W = max(len(r) for r in it["rows"])
    img = [[(0, 0, 0)] * (W*8) for _ in range(H*8)]; used = set(); pal_used = set()
    for r, row in enumerate(it["rows"]):
        for c, (t, pb) in enumerate(row):
            pal = P["pal_base"] + (pb & 0x3F) // 2; hf = pb >> 7 & 1; vf = pb >> 6 & 1
            used.add(t); pal_used.add(pal); px = tile_px(rom, base + it["offs"][t])
            for y in range(8):
                for x in range(8):
                    sx = 7 - x if hf else x; sy = 7 - y if vf else y
                    img[r*8+y][c*8+x] = pals[pal & 0xF][px[sy][sx]]
    write_png(img, out, scale)
    print("extract %06X: cnt %d 쓰인 타일 %d 그림 %d칸×%d행(%d×%dpx) 팔레트 %s 지도 %06X..%06X → %s" % (
        P["item"], it["cnt"], len(used), W, H, W*8, H*8, sorted(pal_used), it["map_start"], it["end"], out))
    return it

def build(rom, P, png, out_rom, grow):
    it = parse_item(rom, P["item"]); H = len(it["rows"]); W = max(len(r) for r in it["rows"])
    w, h, px = read_png(png); assert (w, h) == (W*8, H*8), "PNG 는 %d×%d 이어야 한다" % (W*8, H*8)
    pals = palettes(rom, P.get("pal_tbl"), P); pb0 = P["pal_base"]
    col2pal = {}
    for p in range(16):
        for i, col in enumerate(pals[p]): col2pal.setdefault(col, set()).add(p)
    tiles = []; tile_of = {}; rows = []; errs = []
    for r in range(H):
        row = []
        for c in range(len(it["rows"][r])):
            cell = [px[r*8+y][c*8+x] for y in range(8) for x in range(8)]; cols = set(cell)
            bad = [k for k in cols if k not in col2pal]
            if bad: errs.append("칸(행%d,열%d) 팔레트 표에 없는 색 %s" % (r, c, bad)); row.append((0, 0)); continue
            cand = None
            for p in range(pb0, 16):
                if all(p in col2pal[k] for k in cols): cand = p; break
            if cand is None: errs.append("칸(행%d,열%d) 한 팔레트에 안 드는 색 조합 %s" % (r, c, sorted(cols))); row.append((0, 0)); continue
            idx = {col: i for i, col in enumerate(pals[cand])}
            tb = bytearray()
            for y in range(8):
                wv = 0
                for x in range(8): wv |= swap2(idx[px[r*8+y][c*8+x]]) << (14 - 2*x)
                tb += bytes([wv & 255, wv >> 8])
            tb = bytes(tb)
            # 같은 타일이면 재사용, 좌우/상하 반전으로 같아지면 반전 비트(7/6)로 재사용 — 원본이 그렇게 아낀다
            vals = [[idx[px[r*8+y][c*8+x]] for x in range(8)] for y in range(8)]
            def pack(v):
                o = bytearray()
                for yy in range(8):
                    wv = 0
                    for xx in range(8): wv |= swap2(v[yy][xx]) << (14 - 2*xx)
                    o += bytes([wv & 255, wv >> 8])
                return bytes(o)
            flag = 0
            if tb not in tile_of:
                hf = pack([rr[::-1] for rr in vals]); vf = pack(vals[::-1]); hv = pack([rr[::-1] for rr in vals[::-1]])
                if hf in tile_of: tb, flag = hf, 0x80
                elif vf in tile_of: tb, flag = vf, 0x40
                elif hv in tile_of: tb, flag = hv, 0xC0
                else: tile_of[tb] = len(tiles); tiles.append(tb)
            row.append((tile_of[tb], (cand - pb0) * 2 | flag))
        rows.append(row)
    if errs: print("\n".join(errs)); raise SystemExit("✗ PNG 가 규칙을 어긴다 — 위 칸을 고쳐라 (합치지 않는다)")
    n = len(tiles); print("고유 타일 %d (칸 %d)" % (n, sum(len(r) for r in rows)))
    if n > 256: raise SystemExit("✗ 타일 색인은 1바이트 — 256장 초과")
    cnt = it["cnt"]
    if n > cnt:
        if grow and n <= grow: cnt = n
        else: raise SystemExit("✗ 타일 %d > cnt %d. grow_cnt 로 키워라(아이템 뒤 자리를 먹는다)" % (n, cnt))
    bank = P.get("bank", it["ptr"] - 0x200000); bank_end = P.get("bank_end", bank + 16*n); pbase = it["ptr"] - 0x200000
    # 전부 투명한 타일은 새로 쓰지 않고 뱅크(형제 아이템 공용 구간 포함)에 이미 있는 빈 타일을 가리킨다 — 원본이 그렇게 아낀다
    # ⚠ 공유 빈 타일은 «오프셋 0(ptr 자리)»에 있을 때만 쓴다. 다른 오프셋의 빈 타일을 가리키게 하면 화면이 깨졌다(SS2 rt4: 145칸) —
    #   적재기가 offs[0] 를 특별히 보는 듯. 새 타일은 그 빈 타일을 건너뛰고 놓는다.
    blank = b"\x00" * 16; shared_blank = pbase if rom[pbase:pbase+16] == blank else None
    slots = [off for off in range(bank, bank_end, 16) if off != shared_blank]
    place = []; k = 0
    for tb in tiles:
        if tb == blank and shared_blank is not None: place.append(shared_blank)
        else:
            if k >= len(slots): raise SystemExit("✗ 타일 뱅크 %d B 초과(새 타일 %d장)" % (bank_end - bank, k + 1))
            place.append(slots[k]); k += 1
    rec = bytes([cnt & 255, cnt >> 8]) + it["ptr"].to_bytes(4, "little") + b"".join((place[i] - pbase).to_bytes(2, "little") for i in range(n)) + b"\x00" * (2*(cnt-n)) + bytes([it["hdr"]])
    for row in rows: rec += b"".join(bytes(tp) for tp in row) + b"\xff\xff"
    d = bytearray(rom)
    limit = it["end"] if not grow else P.get("grow_limit", it["end"] + 2*(grow - it["cnt"]))
    assert P["item"] + len(rec) <= limit, "아이템 %d B 가 자리 %d B 를 넘는다" % (len(rec), limit - P["item"])
    d[P["item"]:P["item"]+len(rec)] = rec
    for i, tb in enumerate(tiles):
        if not (tb == blank and shared_blank is not None): d[place[i]:place[i]+16] = tb
    open(out_rom, "wb").write(bytes(d))
    print("build → %s: 아이템 %06X cnt %d(%d 사용) %d B, 타일 %06X..%06X" % (out_rom, P["item"], cnt, n, len(rec), bank, bank+16*n))

if __name__ == "__main__":
    cmd = sys.argv[1]; rom = open(sys.argv[2], "rb").read(); P = load_profile(sys.argv[3])
    if cmd == "extract": extract(rom, P, sys.argv[4], int(sys.argv[5]) if len(sys.argv) > 5 else 1)
    elif cmd == "build": build(rom, P, sys.argv[4], sys.argv[5], int(sys.argv[6]) if len(sys.argv) > 6 else 0)
