#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«원시 워드 지도» 로고 ↔ PNG (아랑전설 F-Contact 타이틀에서 확인). 롬은 읽기만; 쓰기는 사본에만.

형식:  지도 = VRAM 평면 워드 그대로(비트 0~8 타일 색인, 9~12 팔레트, 14 상하반전, 15 좌우반전), W 워드 × H 행, 행 구분 없음.
       타일 = 색인 순으로 «연속»: tile_addr = tiles + 16·idx (아랑 FC: 0x07E493 = 색인 0 기준).
프로파일: {"map":"07FFB1","W":20,"H":16,"tiles":"07E493","pal_dump":".../fct.pal","pal_dump_off":"100","idx_min":1,"idx_max":99}
       idx_min/idx_max = 로고가 쓰는 타일 색인 범위(그 밖의 색인은 다른 그림이 쓰므로 build 가 손대지 않는다)
사용:
    extract <rom> <profile> <out.png> [scale]
    build   <rom_in> <profile> <in.png> <rom_out>
            «최소 변경»: 원본 렌더와 다른 칸만 새 타일로. 새 타일 자리 = idx_min..idx_max 중 «남는 칸이 참조하지 않는» 색인.
            안 바뀐 칸의 워드·타일은 그대로(다른 층·다른 그림과의 공유를 깨지 않는다).
"""
import sys, json
sys.path.insert(0, "/tmp/lang/logo")
import logo_tool as L

def load(path):
    P = json.load(open(path))
    for k in ("map", "tiles", "pal_tbl"):
        if k in P and isinstance(P[k], str): P[k] = int(P[k], 16)
    return P

def words(rom, P):
    return [[rom[P["map"]+2*(r*P["W"]+c)] | (rom[P["map"]+2*(r*P["W"]+c)+1] << 8) for c in range(P["W"])] for r in range(P["H"])]

def render_cell(rom, P, pals, w):
    t = w & 0x1ff; pal = (w >> 9) & 0xF; hf = w >> 15; vf = (w >> 14) & 1
    if not t: return [[(0, 0, 0)] * 8 for _ in range(8)]
    px = L.tile_px(rom, P["tiles"] + 16*t)
    return [[pals[pal][px[7-y if vf else y][7-x if hf else x]] if px[7-y if vf else y][7-x if hf else x] else (0, 0, 0) for x in range(8)] for y in range(8)]

def extract(rom, P, out, scale):
    W, H = P["W"], P["H"]; pals = L.palettes(rom, P.get("pal_tbl"), P); m = words(rom, P)
    img = [[(0, 0, 0)] * (W*8) for _ in range(H*8)]; used = set(); pu = set()
    for r in range(H):
        for c in range(W):
            cell = render_cell(rom, P, pals, m[r][c])
            if m[r][c] & 0x1ff: used.add(m[r][c] & 0x1ff); pu.add((m[r][c] >> 9) & 0xF)
            for y in range(8):
                for x in range(8): img[r*8+y][c*8+x] = cell[y][x]
    L.write_png(img, out, scale)
    print("extract 원시 %06X: %d×%d칸 타일 %d(색인 %d..%d) 팔레트 %s → %s" % (P["map"], W, H, len(used), min(used), max(used), sorted(pu), out))

def pack(v):
    o = bytearray()
    for yy in range(8):
        wv = 0
        for xx in range(8): wv |= v[yy][xx] << (14 - 2*xx)
        o += bytes([wv & 255, wv >> 8])
    return bytes(o)

def build(rom, P, png, out_rom):
    W, H = P["W"], P["H"]; w, h, px = L.read_png(png); assert (w, h) == (W*8, H*8), "PNG 는 %d×%d 이어야 한다" % (W*8, H*8)
    pals = L.palettes(rom, P.get("pal_tbl"), P); allowed = P.get("pals") or list(range(16)); m = words(rom, P)
    lo, hi = P["idx_min"], P["idx_max"]
    changed = []
    for r in range(H):
        for c in range(W):
            cell = [[px[r*8+y][c*8+x] for x in range(8)] for y in range(8)]
            if cell != render_cell(rom, P, pals, m[r][c]): changed.append((r, c, cell))
    kept = {m[r][c] & 0x1ff for r in range(H) for c in range(W) if not any((r, c) == (cr, cc) for cr, cc, _ in changed)}
    free = [i for i in range(lo, hi+1) if i not in kept]
    print("바뀐 칸 %d / %d, 남는 색인 %d (범위 %d..%d)" % (len(changed), W*H, len(free), lo, hi))
    col2pal = {}
    for p in allowed:
        for i, col in enumerate(pals[p]): col2pal.setdefault(col, set()).add(p)
    d = bytearray(rom); new = {}; errs = []
    for r, c, cell in changed:
        cols = {v for row in cell for v in row}
        if cols == {(0, 0, 0)}: m[r][c] = 0; continue
        bad = [k for k in cols if k not in col2pal]
        if bad: errs.append("칸(행%d,열%d) 팔레트 표에 없는 색 %s" % (r, c, bad)); continue
        cand = next((p for p in allowed if all(p in col2pal[k] for k in cols)), None)
        if cand is None: errs.append("칸(행%d,열%d) 한 팔레트에 안 드는 색 조합 %s" % (r, c, sorted(cols))); continue
        idx = {col: i for i, col in enumerate(pals[cand])}
        vals = [[idx[cell[y][x]] for x in range(8)] for y in range(8)]; tb = pack(vals); flag = 0; key = None
        for cand_tb, fl in ((tb, 0), (pack([rr[::-1] for rr in vals]), 0x8000), (pack(vals[::-1]), 0x4000), (pack([rr[::-1] for rr in vals[::-1]]), 0xC000)):
            if cand_tb in new: key, flag = cand_tb, fl; break
        if key is None:
            if not free: errs.append("칸(행%d,열%d) 새 타일 자리 없음 — 색인 %d..%d 소진" % (r, c, lo, hi)); continue
            new[tb] = free.pop(0); key = tb
        ti = new[key]; d[P["tiles"]+16*ti:P["tiles"]+16*ti+16] = key
        m[r][c] = ti | (cand << 9) | flag
    if errs: print("\n".join(errs)); raise SystemExit("✗ 멈춤")
    for r in range(H):
        for c in range(W): d[P["map"]+2*(r*W+c)] = m[r][c] & 255; d[P["map"]+2*(r*W+c)+1] = m[r][c] >> 8
    open(out_rom, "wb").write(bytes(d)); print("build → %s: 새 타일 %d장, 지도 %06X" % (out_rom, len(new), P["map"]))

if __name__ == "__main__":
    cmd = sys.argv[1]; rom = open(sys.argv[2], "rb").read(); P = load(sys.argv[3])
    if cmd == "extract": extract(rom, P, sys.argv[4], int(sys.argv[5]) if len(sys.argv) > 5 else 1)
    elif cmd == "build": build(rom, P, sys.argv[4], sys.argv[5])
