# -*- coding: utf-8 -*-
"""커맨드 화살표 글리프 본을 뜬다 — 카드 3의 → ↓ ←, 카드 66의 ↗.

커맨드 줄의 화살표는 늘 정해진 자리(x 48·49·56·57·64·65·73)에 놓인다.
**그 밖에서 화살표가 나오면 숫자 자리에 잘못 박힌 것**이다(22번 ↓, 66번 ↗).
"""
import io, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cardaudit import rd, lum

D = os.path.expanduser("~/ss2/tmp/cards/shots")


def grab(px, x0, x1, y0, y1):
    return ["".join("#" if lum(px, y, x) > 150 else "." for x in range(x0, x1)) for y in range(y0, y1)]


c3 = rd("%s/d003.png" % D)
c66 = rd("%s/d066.png" % D)
T = {"→": grab(c3, 49, 56, 48, 56),
     "↓": grab(c3, 57, 63, 48, 56),
     "←": grab(c3, 64, 71, 48, 56),
     "↗": grab(c66, 57, 64, 40, 48)}
for k, v in T.items():
    print(k)
    for r in v: print("   " + r)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arrows.json")
io.open(out, "w", encoding="utf-8").write(json.dumps(T, ensure_ascii=False, indent=1))
print("→", out)
