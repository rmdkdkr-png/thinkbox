# -*- coding: utf-8 -*-
"""시안이 화면 어디에 떠 있는지 «찾아서» 견준다.

롬이 다르면 같은 대본도 다른 순간에 닿는다(traps ⑬). 배너가 밀려 뜨면
자리를 손으로 박은 비교는 전부 «어긋남»으로 나온다 — 그건 삽입 실패가 아니다.
그래서 자리를 훑어 **제일 잘 맞는 곳**을 찾고, 거기서 칸별로 센다.
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artdiff import readpng, screen_crop
from cellmatch import learn


def score(a, s):
    m = learn(a, s)
    return sum(1 for i in range(len(a)) if m.get(a[i]) != s[i]), m


def find(art, ppm, x0, y0, span=12):
    W, H, a = readpng(os.path.expanduser(art))
    best = None
    for dy in range(-span, span + 1):
        for dx in range(-span, span + 1):
            x, y = x0 + dx, y0 + dy
            if x < 0 or y < 0 or x + W > 160 or y + H > 152: continue
            s = screen_crop(os.path.expanduser(ppm), x, y, W, H)
            n, m = score(a, s)
            if best is None or n < best[0]: best = (n, x, y, s, m)
    n, x, y, s, m = best
    print("%s ← %s" % (os.path.basename(art), os.path.basename(ppm)))
    print("   제일 잘 맞는 자리 x=%d y=%d (짐작한 자리에서 %+d,%+d) · 다른 화소 %d/%d"
          % (x, y, x - x0, y - y0, n, W * H))
    cols, rows = W // 8, H // 8
    bad = []
    for cy in range(rows):
        for cx in range(cols):
            miss = sum(1 for yy in range(cy * 8, cy * 8 + 8) for xx in range(cx * 8, cx * 8 + 8)
                       if m.get(a[yy * W + xx]) != s[yy * W + xx])
            if miss: bad.append((cy, cx, miss))
    print("   칸 %d개 중 «시안 그대로» %d개" % (cols * rows, cols * rows - len(bad)))
    for cy, cx, k in bad[:8]: print("      어긋난 칸 (행%d, 열%d) — %d/64" % (cy, cx, k))
    print("   색 대응:", m)
    return n, x, y


if __name__ == "__main__":
    find(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]),
         int(sys.argv[5]) if len(sys.argv) > 5 else 12)
