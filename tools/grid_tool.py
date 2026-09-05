#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«격자형» 로고 기록 ↔ PNG (KOF R-2 0x02B986 · SvC 0x38637E 에서 확인). 롬은 읽기만; 쓰기는 사본에만.

기록:  W8 H8 | ptr32(타일 기준 CPU) | cnt16(타일 수) | u16×5(용도 미확인, 그대로 둠) | W×H × (타일, 팔레트바이트)
       행 구분 없음. 오프셋표 없음 — 타일 t 는 ptr + 16·t 에 «연속». 팔레트바이트 = 팔레트×2 (비트7 좌우·비트6 상하 반전은 아이템형과 같다고 가정 — 미검증).
       CPU→파일: ptr < 0x800000 → ptr−0x200000, 아니면(4 MB 롬 상위 뱅크) ptr−0x600000.
       화면 문자RAM 색인 = 타일 + 64 (R-2·SvC 둘 다 실측).
프로파일: {"hdr":"38637E","pal_dump":".../svct.pal","pal_dump_off":"80"}   (pal_tbl 도 됨)
사용:
    extract <rom> <profile> <out.png> [scale]
    build   <rom_in> <profile> <in.png> <rom_out>        타일 수 ≤ cnt(헤더) 여야 한다(연속 자리라 못 늘린다)
"""
import sys, json
sys.path.insert(0, "/tmp/lang/logo")
import logo_tool as L

def f_of(ptr): return ptr - 0x200000 if ptr < 0x800000 else ptr - 0x600000

def parse(rom, hdr):
    W, H = rom[hdr], rom[hdr+1]; ptr = int.from_bytes(rom[hdr+2:hdr+6], "little"); cnt = rom[hdr+6] | (rom[hdr+7] << 8)
    extra = [rom[hdr+8+2*i] | (rom[hdr+9+2*i] << 8) for i in range(5)]
    m0 = hdr + 18; cells = [[(rom[m0+2*(r*W+c)], rom[m0+2*(r*W+c)+1]) for c in range(W)] for r in range(H)]
    return dict(hdr=hdr, W=W, H=H, ptr=ptr, base=f_of(ptr), cnt=cnt, extra=extra, map_start=m0, cells=cells, end=m0 + 2*W*H)

def extract(rom, P, out, scale):
    it = parse(rom, P["hdr"]); pals = L.palettes(rom, P.get("pal_tbl"), P)
    img = [[(0, 0, 0)] * (it["W"]*8) for _ in range(it["H"]*8)]; used = set(); pu = set()
    for r, row in enumerate(it["cells"]):
        for c, (t, pb) in enumerate(row):
            pal = (pb & 0x3F) // 2; hf = pb >> 7 & 1; vf = pb >> 6 & 1; used.add(t); pu.add(pal)
            px = L.tile_px(rom, it["base"] + 16*t)
            for y in range(8):
                for x in range(8):
                    img[r*8+y][c*8+x] = pals[pal & 0xF][px[7-y if vf else y][7-x if hf else x]]
    L.write_png(img, out, scale)
    print("extract 격자 %06X: %d×%d칸(%d×%dpx) cnt %d 쓰인 타일 %d(최대 색인 %d) 타일 %06X.. 팔레트 %s extra %s 지도 %06X..%06X → %s" % (
        it["hdr"], it["W"], it["H"], it["W"]*8, it["H"]*8, it["cnt"], len(used), max(used), it["base"], sorted(pu), ["%04X" % e for e in it["extra"]], it["map_start"], it["end"], out))
    return it

def build(rom, P, png, out_rom):
    it = parse(rom, P["hdr"]); W, H = it["W"], it["H"]
    w, h, px = L.read_png(png); assert (w, h) == (W*8, H*8), "PNG 는 %d×%d 이어야 한다" % (W*8, H*8)
    pals = L.palettes(rom, P.get("pal_tbl"), P); allowed = P.get("pals") or sorted({(pb & 0x3F)//2 for row in it["cells"] for _, pb in row})
    col2pal = {}
    for p in allowed:
        for i, col in enumerate(pals[p & 0xF]): col2pal.setdefault(col, set()).add(p)
    tiles = [b"\x00"*16]; tile_of = {b"\x00"*16: 0}; cells = []; errs = []
    for r in range(H):
        row = []
        for c in range(W):
            cell = [px[r*8+y][c*8+x] for y in range(8) for x in range(8)]; cols = set(cell)
            bad = [k for k in cols if k not in col2pal]
            if bad: errs.append("칸(행%d,열%d) 팔레트 표에 없는 색 %s" % (r, c, bad)); row.append((0, 0)); continue
            cand = next((p for p in allowed if all(p in col2pal[k] for k in cols)), None)
            if cand is None: errs.append("칸(행%d,열%d) 한 팔레트에 안 드는 색 조합 %s" % (r, c, sorted(cols))); row.append((0, 0)); continue
            idx = {col: i for i, col in enumerate(pals[cand & 0xF])}
            vals = [[idx[px[r*8+y][c*8+x]] for x in range(8)] for y in range(8)]
            def pack(v):
                o = bytearray()
                for yy in range(8):
                    wv = 0
                    for xx in range(8): wv |= v[yy][xx] << (14 - 2*xx)
                    o += bytes([wv & 255, wv >> 8])
                return bytes(o)
            tb = pack(vals); flag = 0
            if tb not in tile_of:
                hf = pack([rr[::-1] for rr in vals]); vf = pack(vals[::-1]); hv = pack([rr[::-1] for rr in vals[::-1]])
                if hf in tile_of: tb, flag = hf, 0x80
                elif vf in tile_of: tb, flag = vf, 0x40
                elif hv in tile_of: tb, flag = hv, 0xC0
                else: tile_of[tb] = len(tiles); tiles.append(tb)
            row.append((tile_of[tb], cand * 2 | flag))
        cells.append(row)
    if errs: print("\n".join(errs)); raise SystemExit("✗ PNG 가 규칙을 어긴다 — 위 칸을 고쳐라")
    n = len(tiles); print("고유 타일 %d (칸 %d, 헤더 cnt %d)" % (n, W*H, it["cnt"]))
    if n > it["cnt"]: raise SystemExit("✗ 타일 %d > cnt %d — 연속 자리라 못 늘린다. 같은 8×8 칸을 재사용해 줄여라" % (n, it["cnt"]))
    d = bytearray(rom)
    for i, tb in enumerate(tiles): d[it["base"]+16*i:it["base"]+16*i+16] = tb
    m0 = it["map_start"]
    for r in range(H):
        for c in range(W): d[m0+2*(r*W+c)] = cells[r][c][0]; d[m0+2*(r*W+c)+1] = cells[r][c][1]
    open(out_rom, "wb").write(bytes(d)); print("build → %s: 지도 %06X, 타일 %06X..%06X" % (out_rom, m0, it["base"], it["base"]+16*n))

if __name__ == "__main__":
    cmd = sys.argv[1]; rom = open(sys.argv[2], "rb").read(); P = json.load(open(sys.argv[3]))
    if "hdr" in P and isinstance(P["hdr"], str): P["hdr"] = int(P["hdr"], 16)
    if "pal_tbl" in P and isinstance(P["pal_tbl"], str): P["pal_tbl"] = int(P["pal_tbl"], 16)
    if cmd == "extract": extract(rom, P, sys.argv[4], int(sys.argv[5]) if len(sys.argv) > 5 else 1)
    elif cmd == "build": build(rom, P, sys.argv[4], sys.argv[5])
