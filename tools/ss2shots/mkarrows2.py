# -*- coding: utf-8 -*-
"""커맨드 아이콘 본 여섯을 «화면에 실제로 뜬 그림»에서 뜬다 — 손으로 그리지 않는다.

글 담당이 준 목록: 0xE0~0xE4 다섯 + 0xE7 하나(카드 전체에서 66번 한 번뿐).
뜬 뒤에는 **본마다 몇 번 맞는지 세어** 그 목록의 횟수와 견준다 — 맞으면 본이 옳다는 증명이다.
"""
import io, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cardaudit import rd, lum, BY0, BY1, BX0, BX1

D = os.path.expanduser("~/ss2/tmp/cards/shots")


def grab(card, y0, x0, x1):
    px = rd("%s/d%03d.png" % (D, card))
    return ["".join("#" if lum(px, y, x) > 150 else "." for x in range(x0, x1)) for y in range(y0, y0 + 8)]


T = {"→": grab(3, 48, 49, 56),      # 커맨드 줄에서
     "↓": grab(3, 48, 57, 63),
     "←": grab(3, 48, 64, 71),
     "↘": grab(7, 56, 57, 63),
     "↙": grab(60, 56, 57, 64),
     "↗": grab(66, 40, 57, 64)}     # 66번 그 자리(E7 은 여기 한 번뿐이다)


def count(t):
    h = len(t); w = len(t[0]); n = 0; where = []
    for c in range(1, 121):
        px = rd("%s/d%03d.png" % (D, c))
        for y in range(BY0, BY1 - h):
            for x in range(BX0, BX1 - w):
                ok = True
                for j in range(h):
                    row = t[j]
                    for i in range(w):
                        if (lum(px, y + j, x + i) > 150) != (row[i] == "#"): ok = False; break
                    if not ok: break
                if ok: n += 1; where.append((c, y, x))
    return n, where


if __name__ == "__main__":
    tot = 0
    for k, t in T.items():
        n, w = count(t)
        tot += n
        print("%s 폭%d — %3d회%s" % (k, len(t[0]), n, ("  (%s)" % (w[0],)) if n <= 2 else ""))
    print("합계", tot)
    io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "arrows.json"),
            "w", encoding="utf-8").write(json.dumps(T, ensure_ascii=False, indent=1))
    print("arrows.json 다시 씀 — 본 %d개" % len(T))
