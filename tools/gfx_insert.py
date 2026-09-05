#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SS2 그림 글자 삽입 — 아트 PNG → 칸별 4색 양자화 → 8×8 2bpp 타일 → 롬 «제자리» 덮어쓰기.

    gfx_insert.py build  <in.png> <자산키.json> <롬_in> <롬_out> [--merge]
    gfx_insert.py verify <자산키.json> <롬_a> <롬_b>          두 롬의 그 자산 타일 바이트 비교
    gfx_insert.py shot   <자산키.json> <롬> <out.png>          하니스로 그 화면을 띄워 캡처(태그별 대본 내장)

자산 키 JSON 은 `gfx-ss2/<p|h>_<키>.json` — 이식소가 !vram 덤프에서 뽑은 것:
    {"name","rom","plane","rows":[..],"cols":[..],"cells":[[행,열,타일,팔레트,좌우반전,상하반전]…],
     "tiles":{"타일번호":"롬주소16진|blank|notfound"}, "palettes":{"팔레트":[[r,g,b]×4]}, "budget":{...}}

규칙(어기면 좌표를 대며 멈춘다 — 임의로 합치지 않는다):
  · PNG 크기 = len(cols)*8 × len(rows)*8.
  · 8×8 칸 하나는 팔레트 하나만 쓴다. 그 칸의 팔레트는 JSON 의 셀 값(원본이 쓰던 것)을 그대로 쓴다.
  · 색은 그 팔레트의 4색에 가장 가까운 것으로 양자화한다. 값 0 = 투명(원본이 투명이던 화소는 투명이어야 한다).
  · 고유 타일 수 ≤ 예산(= JSON 의 서로 다른 타일 수). 넘으면 --merge 없이는 멈추고, --merge 면 가장 닮은 칸끼리 합치고 합친 좌표를 보고한다.
  · 반전 셀(좌우/상하)은 원본이 반전으로 재사용하던 칸이다. 새 그림에서도 같은 반전 관계가 유지되는지 검사하고, 깨지면 그 칸은 «반전 안 씀»으로 새 타일을 요구한다(예산 초과 판정에 포함).
  · 롬 쓰기는 JSON 의 타일 주소(`tiles`)에만 한다. blank/notfound 타일은 안 건드린다(공용 타일일 수 있다).
"""
import sys, os, json, struct, zlib, collections


def read_png(path):
    d = open(path, "rb").read()
    assert d[:8] == b"\x89PNG\r\n\x1a\n", "PNG 아님"
    pos = 8; idat = b""; w = h = ct = bd = 0; pal = b""; trns = b""
    while pos < len(d):
        n = struct.unpack(">I", d[pos:pos + 4])[0]; t = d[pos + 4:pos + 8]; body = d[pos + 8:pos + 8 + n]; pos += 12 + n
        if t == b"IHDR": w, h, bd, ct = struct.unpack(">IIBB", body[:10])
        elif t == b"PLTE": pal = body
        elif t == b"tRNS": trns = body
        elif t == b"IDAT": idat += body
    assert bd == 8, "8비트 PNG 만"
    raw = zlib.decompress(idat)
    bpp = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ct]
    stride = w * bpp; out = []; prev = bytearray(stride)
    p = 0
    for y in range(h):
        f = raw[p]; p += 1; line = bytearray(raw[p:p + stride]); p += stride
        for i in range(stride):
            a = line[i - bpp] if i >= bpp else 0; b = prev[i]; c = prev[i - bpp] if i >= bpp else 0
            if f == 1: line[i] = (line[i] + a) & 255
            elif f == 2: line[i] = (line[i] + b) & 255
            elif f == 3: line[i] = (line[i] + (a + b) // 2) & 255
            elif f == 4:
                pp = a + b - c; pa = abs(pp - a); pb = abs(pp - b); pc = abs(pp - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else (b if pb <= pc else c))) & 255
        prev = line
        row = []
        for x in range(w):
            if ct == 2: row.append((line[x * 3], line[x * 3 + 1], line[x * 3 + 2], 255))
            elif ct == 6: row.append((line[x * 4], line[x * 4 + 1], line[x * 4 + 2], line[x * 4 + 3]))
            elif ct == 3:
                i = line[x]; row.append((pal[i * 3], pal[i * 3 + 1], pal[i * 3 + 2], trns[i] if i < len(trns) else 255))
            else: row.append((line[x], line[x], line[x], 255))
        out.append(row)
    return w, h, out


MAGENTA = (255, 0, 255)


def quant(px, palette):
    """화소 → 팔레트 색인 0..3. 투명(알파 0 또는 자홍) → 0."""
    r, g, b, a = px
    if a < 128 or (r, g, b) == MAGENTA: return 0
    best = 1; bd = None
    for i in range(1, 4):
        pr, pg, pb = palette[i]
        d = (r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2
        if bd is None or d < bd: bd = d; best = i
    # 팔레트의 0번 색과도 견준다(원본이 0번을 «검정»으로 쓰는 칸이 있다)
    pr, pg, pb = palette[0]
    if (r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2 < bd: best = 0
    return best


def cell_tile(rows, r0, c0, palette):
    """8×8 칸 → 픽셀 값 8×8 (0..3)"""
    return [[quant(rows[r0 + y][c0 + x], palette) for x in range(8)] for y in range(8)]


def flip(t, hf, vf):
    o = [r[::-1] for r in t] if hf else [r[:] for r in t]
    if vf: o = o[::-1]
    return o


def pack(t):
    """8×8 값 → 16B 2bpp(행 워드 LE, 화소 x 의 비트 (15−2x,14−2x))"""
    out = bytearray()
    for y in range(8):
        w = 0
        for x in range(8): w |= (t[y][x] & 3) << (14 - 2 * x)
        out += bytes([w & 0xFF, (w >> 8) & 0xFF])
    return bytes(out)


def build(png, cardpath, rom_in, rom_out, merge=False):
    card = json.load(open(cardpath, encoding="utf-8"))
    rows_i = card["rows"]; cols_i = card["cols"]
    W, H, px = read_png(png)
    assert (W, H) == (len(cols_i) * 8, len(rows_i) * 8), "PNG 크기 %dx%d ≠ 요구 %dx%d" % (W, H, len(cols_i) * 8, len(rows_i) * 8)
    pals = {int(k): [tuple(c) for c in v] for k, v in card["palettes"].items()}
    addr = {int(k): (int(v, 16) if v not in ("blank", "notfound") else None) for k, v in card["tiles"].items()}
    # 셀 순회 → 타일 번호별로 «그 타일이 그려야 할 그림»을 모은다(반전은 되돌려서 비교)
    want = {}; conflicts = []
    for r, c, t, p, hf, vf in card["cells"]:
        ri = rows_i.index(r); ci = cols_i.index(c)
        cell = cell_tile(px, ri * 8, ci * 8, pals[p])
        base = flip(cell, hf, vf)          # 화면 그림 → 저장 그림(반전 되돌리기)
        if t in want and want[t] != base: conflicts.append((r, c, t))
        want.setdefault(t, base)
    writable = [t for t in want if addr.get(t) is not None]
    budget = len(writable)
    uniq = len({bytes(pack(v)) for t, v in want.items() if addr.get(t) is not None})
    report = {"칸": len(card["cells"]), "타일 자리(쓸 수 있는)": budget, "새 그림 고유 타일": uniq,
              "반전 충돌 칸": conflicts, "공용/빈 타일(안 건드림)": [t for t in want if addr.get(t) is None]}
    if conflicts and not merge:
        print("★ 반전 재사용 칸이 새 그림에서 깨진다(같은 타일 번호인데 그림이 다르다):", conflicts[:10])
        print("   --merge 를 주면 첫 칸 그림으로 통일한다(그 칸들은 원본과 달라진다).")
        return report, None
    b = bytearray(open(rom_in, "rb").read())
    wrote = 0
    for t, v in want.items():
        a = addr.get(t)
        if a is None: continue
        b[a:a + 16] = pack(v); wrote += 1
    open(rom_out, "wb").write(bytes(b))
    report["쓴 타일"] = wrote
    report["쓴 범위"] = "%06X~%06X" % (min(a for a in addr.values() if a is not None), max(a for a in addr.values() if a is not None) + 16)
    return report, rom_out


def verify(cardpath, rom_a, rom_b):
    card = json.load(open(cardpath, encoding="utf-8"))
    A = open(rom_a, "rb").read(); B = open(rom_b, "rb").read()
    diff = []
    for k, v in card["tiles"].items():
        if v in ("blank", "notfound"): continue
        a = int(v, 16)
        if A[a:a + 16] != B[a:a + 16]: diff.append((int(k), "%06X" % a))
    return diff


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "build":
        merge = "--merge" in sys.argv
        rep, out = build(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], merge)
        for k, v in rep.items(): print("%s: %s" % (k, v))
        print("→", out if out else "(안 씀)")
    elif cmd == "verify":
        d = verify(sys.argv[2], sys.argv[3], sys.argv[4])
        print("다른 타일 %d개%s" % (len(d), (": " + str(d[:12])) if d else " — 바이트 0 차이"))
    else:
        print(__doc__)
