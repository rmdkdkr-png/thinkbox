#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""격자형 기록 «최소 변경» 삽입 — 바뀐 칸만 새 타일로, 안 바뀐 칸은 원본 (타일, 팔레트) 그대로.

    grid_build2.py <rom_in> <profile> <in.png> <rom_out>

왜: 격자형은 지도가 «기록의 cnt 밖 색인»(다른 그림이 실어 둔 타일)도 참조하고, 타일이 연속이라 색인을 다시 매기면
    같은 뱅크를 쓰는 다른 화면 요소가 깨진다(R-2·SvC 왕복에서 확인). 그래서 지도 색인은 건드리지 않고,
    «바뀐 칸»에만 기록 자기 범위(0..cnt−1) 안에서 안 쓰는 색인을 배정한다.
    안 쓰는 색인 = 0..cnt−1 중 «변경 뒤에도 남는 칸»이 참조하지 않는 것. 예산이 모자라면 좌표를 대며 멈춘다.
"""
import sys, json
sys.path.insert(0, "/tmp/lang/logo")
import logo_tool as L, grid_tool as G

def pack(v):
    o = bytearray()
    for yy in range(8):
        wv = 0
        for xx in range(8): wv |= v[yy][xx] << (14 - 2*xx)
        o += bytes([wv & 255, wv >> 8])
    return bytes(o)

def main():
    rom = open(sys.argv[1], "rb").read(); P = json.load(open(sys.argv[2]))
    if isinstance(P["hdr"], str): P["hdr"] = int(P["hdr"], 16)
    if "pal_tbl" in P and isinstance(P["pal_tbl"], str): P["pal_tbl"] = int(P["pal_tbl"], 16)
    it = G.parse(rom, P["hdr"]); W, H = it["W"], it["H"]; pals = L.palettes(rom, P.get("pal_tbl"), P)
    w, h, px = L.read_png(sys.argv[3]); assert (w, h) == (W*8, H*8), "PNG 는 %d×%d 이어야 한다" % (W*8, H*8)
    # 원본 렌더(칸별)와 비교
    def render(t, pb):
        pal = (pb & 0x3F)//2; hf = pb >> 7 & 1; vf = pb >> 6 & 1; tp = L.tile_px(rom, it["base"] + 16*t)
        return [[pals[pal & 0xF][tp[7-y if vf else y][7-x if hf else x]] for x in range(8)] for y in range(8)]
    changed = []
    for r in range(H):
        for c in range(W):
            t, pb = it["cells"][r][c]; orig = render(t, pb)
            cell = [[px[r*8+y][c*8+x] for x in range(8)] for y in range(8)]
            if cell != orig: changed.append((r, c, cell))
    keep_idx = {it["cells"][r][c][0] for r in range(H) for c in range(W) if not any((r, c) == (cr, cc) for cr, cc, _ in changed)}
    free = [i for i in range(it["cnt"]) if i not in keep_idx]
    print("바뀐 칸 %d / %d, 남는 색인 %d (cnt %d)" % (len(changed), W*H, len(free), it["cnt"]))
    allowed = P.get("pals") or sorted({(pb & 0x3F)//2 for row in it["cells"] for _, pb in row})
    col2pal = {}
    for p in allowed:
        for i, col in enumerate(pals[p & 0xF]): col2pal.setdefault(col, set()).add(p)
    d = bytearray(rom); new_tiles = {}; errs = []; m0 = it["map_start"]
    for r, c, cell in changed:
        cols = {v for row in cell for v in row}
        bad = [k for k in cols if k not in col2pal]
        if bad: errs.append("칸(행%d,열%d) 팔레트 표에 없는 색 %s" % (r, c, bad)); continue
        cand = next((p for p in allowed if all(p in col2pal[k] for k in cols)), None)
        if cand is None: errs.append("칸(행%d,열%d) 한 팔레트에 안 드는 색 조합 %s" % (r, c, sorted(cols))); continue
        idx = {col: i for i, col in enumerate(pals[cand & 0xF])}
        vals = [[idx[cell[y][x]] for x in range(8)] for y in range(8)]; tb = pack(vals); flag = 0
        # 이미 새로 만든 타일과 같거나 반전이면 재사용
        key = None
        for cand_tb, fl in ((tb, 0), (pack([rr[::-1] for rr in vals]), 0x80), (pack(vals[::-1]), 0x40), (pack([rr[::-1] for rr in vals[::-1]]), 0xC0)):
            if cand_tb in new_tiles: key, flag = cand_tb, fl; break
        if key is None:
            if not free: errs.append("칸(행%d,열%d) 새 타일 자리 없음 — 예산 %d 소진" % (r, c, it["cnt"])); continue
            new_tiles[tb] = free.pop(0); key = tb
        ti = new_tiles[key]
        d[it["base"]+16*ti:it["base"]+16*ti+16] = key
        d[m0+2*(r*W+c)] = ti; d[m0+2*(r*W+c)+1] = (cand * 2) | flag
    if errs: print("\n".join(errs)); raise SystemExit("✗ 멈춤")
    open(sys.argv[4], "wb").write(bytes(d))
    print("build2 → %s: 새 타일 %d장, 지도 %06X" % (sys.argv[4], len(new_tiles), m0))

main()
