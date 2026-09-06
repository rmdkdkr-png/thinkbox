# -*- coding: utf-8 -*-
"""톤별 화소 수 — **양쪽이 같은 도구로 재야** 숫자가 맞는다.

왜 필요한가: 같은 승부를 두고 한쪽은 「밝은 1899 · 55:7:38」, 한쪽은 「2000 · 65:8:26」이 나왔다.
그림이 달라서가 아니라 **세는 법이 달라서**다. 톤 경계를 어디로 잡느냐만 달랐다.
숫자로 다투기 전에 **자를 맞춰라.**

세는 법(이 파일이 정본):
  · 화면 PPM 이든 시안 PNG 이든 **네 갈래**로만 나눈다 — 투명 / 밝은 / 중간 / 어두운
  · 붉은 판·흰 판 둘 다 받는다(2·3회전은 흰 계열이다)
  · 경계는 **밝기(가장 큰 채널)** 로 가른다: >200 밝은 · 120~200 중간 · 40~120 어두운 · ≤40 투명

쓰는 법:
  python3 tonecount.py <파일> [x0 y0 w h]      # .ppm 이면 화면, .png 면 시안
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# 배너 잉크는 이 세 색뿐이다(화면에서 실측 — 배너 있는/없는 프레임의 차이로 뽑았다).
# ⚠ **밝기로 가르면 안 된다** — 배경 하늘까지 「밝은」으로 센다. 실제로 그렇게 재서
#   승부 밝은 색이 2898 로 나왔는데 잉크만 세면 1972 다. 색을 못 박아야 한다.
INK = {(255, 0, 0): "밝은", (172, 0, 0): "중간", (65, 0, 0): "어두운"}
# 시안 PNG 쪽 대응(회색 네 갈래)
ART = {(255, 255, 255): "밝은", (170, 170, 170): "중간", (68, 68, 68): "어두운"}


def classify(c):
    t = tuple(c)
    return INK.get(t) or ART.get(t)


def count(path, box=None):
    p = os.path.expanduser(path)
    if p.lower().endswith(".ppm"):
        import bannerpick as B
        px = B.ppm(p); W = 160
        x0, y0, w, h = box if box else (0, 0, 160, 152)
        get = lambda x, y: tuple(px[((y0 + y) * W + (x0 + x)) * 3:((y0 + y) * W + (x0 + x)) * 3 + 3])
    else:
        from artdiff import readpng
        W, H, a = readpng(p)
        x0, y0, w, h = box if box else (0, 0, W, H)
        get = lambda x, y: a[(y0 + y) * W + (x0 + x)]
    n = {"밝은": 0, "중간": 0, "어두운": 0}
    for y in range(h):
        for x in range(w):
            k = classify(get(x, y))
            if k: n[k] += 1
    return n


def show(path, box=None, label=""):
    import hashlib
    p = os.path.expanduser(path)
    md5 = hashlib.md5(open(p, "rb").read()).hexdigest()[:12]
    n = count(path, box)
    t = sum(n.values())
    print("  %s%s · md5 %s" % ((label + " ") if label else "", p, md5))
    print("     밝은 %5d · 중간 %5d · 어두운 %5d · 합 %5d   %s"
          % (n["밝은"], n["중간"], n["어두운"], t,
             ("%.0f : %.0f : %.0f" % tuple(100 * n[k] / t for k in ("밝은", "중간", "어두운"))) if t else "—"))
    return n


if __name__ == "__main__":
    box = tuple(int(x) for x in sys.argv[2:6]) if len(sys.argv) >= 6 else None
    show(sys.argv[1], box)
