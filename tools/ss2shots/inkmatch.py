# -*- coding: utf-8 -*-
"""«잉크 자리»로 견준다 — 시안의 투명 칸 뒤는 게임 배경이라 색이 매번 다르다.

색을 통째로 견주면 배경(하늘·산·바닥)이 전부 «어긋남»으로 잡힌다. 그건 삽입 실패가 아니다.
그래서 ⓐ 글자가 있는 자리가 같은가 ⓑ 글자 농담이 한 짝으로 일관되게 옮았나 — 둘만 본다.
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artdiff import readpng, screen_crop

TRANS = (0, 0, 0)   # 시안의 투명색


def run(art, ppm, x0, y0):
    import stamp
    stamp.head("잉크 대조", 시안=art, 화면=ppm)      # ★ 무엇을 쟀는지 먼저 찍는다
    W, H, a = readpng(os.path.expanduser(art))
    s = screen_crop(os.path.expanduser(ppm), x0, y0, W, H)
    # 시안 잉크색 → 화면색 짝 (잉크 화소만 모은다)
    pair = collections.defaultdict(collections.Counter)
    for i in range(len(a)):
        if a[i] != TRANS: pair[a[i]][s[i]] += 1
    m = {c: cc.most_common(1)[0][0] for c, cc in pair.items()}
    ink = set(m.values())
    # ★ 배너가 «번쩍이는» 프레임이 있다(뜰 때 한 색으로 하얘진다). 그 프레임에서 재면
    #   농담이 전부 한 색으로 뭉쳐 「농담 어긋남 0」이 **거짓으로 통과**한다.
    #   그래서 뭉친 것은 통과가 아니라 **못 잰 것**으로 소리 내어 알린다.
    flat = len(ink) != len(m)
    if flat:
        print("   ⚠⚠ 농담을 **못 쟀다** — 시안 농담 %d 가지가 화면 색 %d 가지로 뭉쳤다."
              " 배너가 번쩍이는 순간이다. **다른 프레임에서 다시 재라.**" % (len(m), len(ink)))
    miss_pos = miss_shade = 0
    cells = collections.Counter()
    for i in range(len(a)):
        want_ink = a[i] != TRANS
        got_ink = s[i] in ink
        cy, cx = (i // W) // 8, (i % W) // 8
        if want_ink != got_ink:
            miss_pos += 1; cells[(cy, cx)] += 1
        elif want_ink and s[i] != m[a[i]]:
            miss_shade += 1; cells[(cy, cx)] += 1
    n_ink = sum(1 for c in a if c != TRANS)
    cols, rows = W // 8, H // 8
    print("%s ← %s  (x=%d y=%d)" % (os.path.basename(art), os.path.basename(ppm), x0, y0))
    print("   잉크 화소 %d개 · 자리 어긋남 %d · 농담 %s · **맞은 화소 %d/%d**"
          % (n_ink, miss_pos, "못 잼(번쩍임)" if flat else "어긋남 %d" % miss_shade,
             W * H - miss_pos - miss_shade, W * H))
    print("   칸 %d개 중 «시안 그대로» %d개" % (cols * rows, cols * rows - len(cells)))
    for (cy, cx), k in sorted(cells.items())[:8]:
        print("      어긋난 칸 (행%d, 열%d) — %d/64" % (cy, cx, k))
    print("   농담 짝:", ", ".join("%s→%s ×%d" % (k, m[k], sum(pair[k].values())) for k in sorted(m)))


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
