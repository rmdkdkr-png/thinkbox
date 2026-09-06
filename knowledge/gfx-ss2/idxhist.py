# -*- coding: utf-8 -*-
"""표마다 «화소 색인 0/1/2/3» 을 센다 — 「진회색이 획이냐 바탕이냐」를 끝내는 표.

기록 안에는 팔레트 바이트가 **없다**(머리 = cnt16|ptr32|off16×cnt|행수16|행들, 바이트가 딱 맞다).
팔레트는 스크롤면 칸말(비트 12~15)이 정하고 그건 코드 쪽이다.
그러니 여기서 낼 수 있는 것은 **색인별 화소 수**이고, 그것으로 충분하다 —
화면 실측에서 **색인 1 = 가장 밝은 색 = 획 본체**임이 이미 잡혔기 때문이다
(순정 「승부」: 밝은 1972 · 중간 250 · 어두운 782, tools/ss2shots/tonecount.py).
"""
import os, struct

ROM = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")
KOR = os.path.expanduser("~/ss2/rom/ss2.ngc")
TB, BASE = 0x06F56D, 0x05F56D


def rec(rom, i):
    v = rom[TB + 2 * i] | (rom[TB + 2 * i + 1] << 8); a = BASE + v
    cnt = rom[a] | (rom[a + 1] << 8)
    base = struct.unpack("<I", rom[a + 2:a + 6])[0] - 0x200000
    o = a + 6
    off = [rom[o + 2 * j] | (rom[o + 2 * j + 1] << 8) for j in range(cnt)]
    p = o + 2 * cnt
    nrow = rom[p] | (rom[p + 1] << 8); p += 2
    rows = []
    for _ in range(nrow):
        L = []
        while rom[p] != 0xFF: L.append(rom[p]); p += 1
        p += 1
        rows.append([None] + L)
    return base, off, rows


def hist(rom, i):
    base, off, rows = rec(rom, i)
    h = [0, 0, 0, 0]
    for r in rows:
        for c in r:
            if c is None or c >= len(off):
                h[0] += 64; continue     # 암묵 빈 칸은 통째로 투명
            a = base + off[c]
            for y in range(8):
                w = (rom[a + y * 2] << 8) | rom[a + y * 2 + 1]
                for x in range(8):
                    h[(w >> (14 - 2 * x)) & 3] += 1
    w = max(len(r) for r in rows) * 8
    return h, w, len(rows) * 8


pr = open(ROM, "rb").read()
kr = open(KOR, "rb").read() if os.path.exists(KOR) else None

print("표  크기      | 순정: 투명   색인1(획)  색인2   색인3 | 잉크계 | 한글: 색인1  잉크계 | 획 비")
print("-" * 108)
for i in range(48):
    try:
        h, W, H = hist(pr, i)
    except Exception:
        continue
    ink = h[1] + h[2] + h[3]
    kt = ""
    if kr:
        try:
            k, _, _ = hist(kr, i)
            ki = k[1] + k[2] + k[3]
            rate = (100.0 * k[1] / h[1]) if h[1] else 0
            kt = "| %5d %6d | %3.0f%%" % (k[1], ki, rate)
        except Exception:
            kt = "| (못읽음)"
    print("%2d %3dx%-3d | %6d %8d %7d %7d | %6d %s"
          % (i, W, H, h[0], h[1], h[2], h[3], ink, kt))
