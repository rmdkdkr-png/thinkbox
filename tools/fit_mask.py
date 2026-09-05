#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""이식소 마스크(칸당 16px, 흰=자유)에 맞춰 글자를 «칸 안에» 앉힌다.

    python3 fit_mask.py <마스크.png> <글자1.png> [<글자2.png> ...] <out.png> [--ink R,G,B --rim R,G,B]

각 글자 PNG 는 생성본(흰 글자/검은 바탕)이고, 마스크의 «자유 칸이 연속으로 이어진 세로 띠»를
글자 수만큼 나눠 각 글자를 그 띠에 꽉 차게 앉힌다. 자유 칸 밖은 자홍(투명)으로 남긴다.
"""
import sys

from PIL import Image, ImageFilter

args = [a for a in sys.argv[1:]]
ink = (255, 0, 0)
rim = (68, 0, 0)
if '--ink' in args:
    k = args.index('--ink')
    ink = tuple(int(v) for v in args[k + 1].split(','))
    del args[k:k + 2]
weights = None
fill = '--fill' in args
union = '--union' in args
if union:
    args.remove('--union')
if fill:
    args.remove('--fill')
if '--weights' in args:
    k = args.index('--weights')
    weights = [float(v) for v in args[k + 1].split(',')]
    del args[k:k + 2]
if '--rim' in args:
    k = args.index('--rim')
    rim = tuple(int(v) for v in args[k + 1].split(','))
    del args[k:k + 2]
mask_p, out_p = args[0], args[-1]
glyph_ps = args[1:-1]

if mask_p.endswith('.json'):
    # 자산 JSON 에서 «자유 칸»을 직접 계산한다(그 칸만의 타일 · 반전 아님 · blank 아님)
    import json
    card = json.load(open(mask_p, encoding='utf-8'))
    rws, cls = card['rows'], card['cols']
    rows, cols = len(rws), len(cls)
    r0m, c0m = min(rws), min(cls)
    use = {}
    for r, c, t, pal, hf, vf in card['cells']:
        use.setdefault(t, []).append((r, c, hf, vf))
    free = [[False] * cols for _ in range(rows)]
    for t, cs in use.items():
        addr = card['tiles'].get(str(t))
        if addr in (None, 'blank', 'notfound') or len(cs) != 1:
            continue
        r, c, hf, vf = cs[0]
        if hf or vf:
            continue
        free[r - r0m][c - c0m] = True
else:
    m = Image.open(mask_p).convert('RGB')
    CW = 16                                # 마스크 PNG 는 칸당 16px
    cols, rows = m.width // CW, m.height // CW
    free = [[m.getpixel((c * CW + CW // 2, r * CW + CW // 2))[0] > 200
             and m.getpixel((c * CW + CW // 2, r * CW + CW // 2))[1] > 200 for c in range(cols)] for r in range(rows)]
W, H = cols * 8, rows * 8

free_rows = [r for r in range(rows) if any(free[r])]
r0, r1 = min(free_rows), max(free_rows) + 1
# 글자마다 띠 높이를 다르게 줄 수 있다(--weights 1,2,2) — 「1」처럼 좁은 글자에 자리를 덜 준다
ws = weights or [1.0] * len(glyph_ps)
tot = sum(ws)
edges = [r0]
acc = 0.0
for w in ws:
    acc += w
    edges.append(r0 + round((r1 - r0) * acc / tot))
art = Image.new('RGB', (W, H), (255, 0, 255))

for i, gp in enumerate(glyph_ps):
    br0, br1 = edges[i], edges[i + 1]
    # 띠 안의 «모든 행»에서 자유로운 열만 쓴다 — 한 행이라도 막힌 열은 글자가 잘린다
    if union:
        # 자유 칸의 «바깥 상자»를 쓴다 — 글자를 크게 앉히고, 모서리는 마스크가 깎는다
        cs = [c for c in range(cols) if any(free[r][c] for r in range(br0, br1))]
    else:
        cs = [c for c in range(cols) if all(free[r][c] for r in range(br0, br1))]
    if not cs:
        continue
    c0, c1 = min(cs), max(cs) + 1
    bw, bh = (c1 - c0) * 8, (br1 - br0) * 8
    # ★ 먼저 2값화한 뒤 줄인다 — 가는 획은 평균이 문턱을 못 넘어 사라진다(실측).
    src = Image.open(gp).convert('L').point(lambda v: 255 if v > 90 else 0)
    bb = src.getbbox()
    src = src.crop(bb)
    tw, th = max(1, bw - 2), max(1, bh - 2)
    if fill:
        g = src.resize((tw, th), Image.BOX)           # 칸을 꽉 채운다(원본 한자처럼)
    else:
        sc = min(tw / src.width, th / src.height)     # 비율을 지켜 앉힌다
        g = src.resize((max(1, round(src.width * sc)), max(1, round(src.height * sc))), Image.BOX)
    g = g.point(lambda v: 255 if v > 70 else 0)
    ox, oy = 1 + (tw - g.width) // 2, 1 + (th - g.height) // 2
    layer = Image.new('RGB', (bw, bh), (255, 0, 255))
    layer.paste(Image.new('RGB', g.size, rim), (ox, oy), g.filter(ImageFilter.MaxFilter(3)))
    layer.paste(Image.new('RGB', g.size, ink), (ox, oy), g)
    art.paste(layer, (c0 * 8, br0 * 8))

# 자유 칸 밖은 투명으로
ap = art.load()
for r in range(rows):
    for c in range(cols):
        if not free[r][c]:
            for y in range(r * 8, r * 8 + 8):
                for x in range(c * 8, c * 8 + 8):
                    ap[x, y] = (255, 0, 255)
art.save(out_p)
art.resize((W * 4, H * 4), Image.NEAREST).save(out_p.replace('.png', '_4x.png'))
print('→ %s (%d×%d · 자유 칸 %d)' % (out_p, W, H, sum(sum(r) for r in free)))
