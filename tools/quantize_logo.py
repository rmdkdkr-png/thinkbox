#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""아무 RGB 그림 → 기기 규칙을 100% 지킨 로고 PNG (logo_tool build 가 안 멈추는 입력).

    quantize_logo.py <art.png> <rom> <profile.json> <out.png> [--orig 원본.png --mask 마스크.png] [--pals 4,5,6,...] [--map out_map.png]

규칙: 캔버스 = 아이템 칸×8 × 행×8(예: 160×88). 8×8 칸마다 허용 팔레트 중 «오차 합이 가장 작은 하나»를 고르고,
      칸 안 픽셀은 그 팔레트 4색 중 가장 가까운 색으로(디더 없음). 마스크가 흰 픽셀은 원본 PNG 픽셀을 그대로 둔다(칼·불꽃·리본 보존).
      마스크로 보존한 픽셀도 칸의 팔레트 선택에 들어간다(보존 색과 새 색이 한 팔레트에 들도록).
입력 크기가 다르면 상자 평균(area)으로 캔버스 크기에 맞춘다. 배경(검정) = 색 0 = 투명.
출력: out.png(양자화 결과), out_map.png(칸별 팔레트 번호를 색띠로), 통계(칸별 오차·원본과의 픽셀 차이).
"""
import sys, json
sys.path.insert(0, "/tmp/lang/logo")
import logo_tool as L

def resize_area(px, W, H):
    h = len(px); w = len(px[0])
    if (w, h) == (W, H): return px
    out = []
    for Y in range(H):
        y0 = Y * h / H; y1 = (Y + 1) * h / H; row = []
        for X in range(W):
            x0 = X * w / W; x1 = (X + 1) * w / W; acc = [0.0, 0.0, 0.0]; n = 0.0
            for y in range(int(y0), min(h, int(y1 - 1e-9) + 1)):
                fy = min(y1, y + 1) - max(y0, y)
                for x in range(int(x0), min(w, int(x1 - 1e-9) + 1)):
                    fx = min(x1, x + 1) - max(x0, x); f = fx * fy
                    if f <= 0: continue
                    for k in range(3): acc[k] += px[y][x][k] * f
                    n += f
            row.append(tuple(int(round(a / n)) for a in acc) if n else (0, 0, 0))
        out.append(row)
    return out

def d2(a, b): return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def main():
    args = sys.argv[1:]; art, rom_path, prof, out = args[:4]; opts = {}
    i = 4
    while i < len(args):
        if args[i].startswith("--"): opts[args[i][2:]] = args[i+1]; i += 2
        else: i += 1
    rom = open(rom_path, "rb").read(); P = L.load_profile(prof); it = L.parse_item(rom, P["item"])
    H = len(it["rows"]); W = max(len(r) for r in it["rows"]); pals = L.palettes(rom, P.get("pal_tbl"), P)
    allowed = [int(x) for x in opts["pals"].split(",")] if "pals" in opts else sorted({P["pal_base"] + (pb & 0x3F)//2 for row in it["rows"] for _, pb in row})
    w, h, px = L.read_png(art); px = resize_area(px, W*8, H*8)
    orig = mask = None
    if "orig" in opts: _, _, orig = L.read_png(opts["orig"])
    if "mask" in opts: _, _, mask = L.read_png(opts["mask"])
    keep = lambda x, y: mask is not None and orig is not None and mask[y][x][0] > 127
    res = [[(0, 0, 0)] * (W*8) for _ in range(H*8)]; palmap = [[None] * W for _ in range(H)]; cell_err = []
    for r in range(H):
        for c in range(len(it["rows"][r])):
            cells = [(x, y) for y in range(r*8, r*8+8) for x in range(c*8, c*8+8)]
            best = None
            for p in allowed:
                cols = pals[p & 0xF]; err = 0; ok = True
                for x, y in cells:
                    src = orig[y][x] if keep(x, y) else px[y][x]
                    if keep(x, y):
                        if src not in cols: ok = False; break
                    else: err += min(d2(src, k) for k in cols)
                if ok and (best is None or err < best[0]): best = (err, p)
            if best is None: raise SystemExit("칸(행%d,열%d): 보존 픽셀 색이 어느 허용 팔레트에도 없다" % (r, c))
            err, p = best; palmap[r][c] = p; cell_err.append(err); cols = pals[p & 0xF]
            for x, y in cells:
                src = orig[y][x] if keep(x, y) else px[y][x]
                res[y][x] = src if keep(x, y) else min(cols, key=lambda k: d2(src, k))
    L.write_png(res, out)
    # 팔레트 지도 그림: 칸을 팔레트 번호 색으로
    tint = {4:(255,0,0),5:(255,140,0),6:(255,90,0),7:(0,0,255),8:(90,90,180),9:(150,150,200),10:(40,120,60),11:(255,200,100),12:(180,20,20),
            0:(0,0,255),1:(255,0,0),2:(255,120,0),3:(200,0,60),13:(120,120,120),14:(120,0,200),15:(200,180,0)}
    mp = [[(0, 0, 0)] * (W*8) for _ in range(H*8)]
    for r in range(H):
        for c in range(W):
            p = palmap[r][c]
            if p is None: continue
            for y in range(r*8, r*8+8):
                for x in range(c*8, c*8+8): mp[y][x] = tint.get(p, (255, 255, 255)) if (x % 8 and y % 8) else (30, 30, 30)
    L.write_png(mp, opts.get("map", out.replace(".png", "_map.png")), 3)
    stats = "칸 %d 허용 팔레트 %s 칸 오차 합 평균 %.0f 최대 %.0f" % (len(cell_err), allowed, sum(cell_err)/len(cell_err), max(cell_err))
    if orig is not None:
        diff = sum(1 for y in range(H*8) for x in range(W*8) if res[y][x] != orig[y][x]); tot = W*8*H*8
        stats += " | 원본과 다른 픽셀 %d/%d (%.1f%%)" % (diff, tot, 100.0*diff/tot)
    print(stats); print("→", out)

main()
