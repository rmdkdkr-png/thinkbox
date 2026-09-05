# -*- coding: utf-8 -*-
"""배너의 «자리 규격»을 화면에서 잰다 — 롬 주소 대역을 미리 정하지 않는다.

대역으로 거르면 **그 대역 밖에 실린 조각을 통째로 놓친다.** 승부가 그랬다 —
윗 두 줄이 0x06CBxx 에 따로 실려 있어서 6×12 를 6×10 으로 잘못 쟀다.

그래서 «배너가 있는 프레임»과 «없는 프레임»의 칸을 견줘 다른 칸만 모은다.
배경이 그대로인 화면이라 다른 칸 = 배너다.
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vrdec

ROWS, COLS = range(19), range(20)


def cellmap(d, plane=0):
    m = {}
    for r in ROWS:
        for c in COLS:
            t = vrdec.cell(d["scroll"], plane, r, c)[0]
            m[(r, c)] = (t, d["char"][t * 16:t * 16 + 16])
    return m


def quiet_tag(dd, tags, target):
    """가장 «비어 있는» 프레임을 바탕으로 고른다 — 배너가 없는 순간."""
    best = None
    for t in tags:
        if t == target: continue
        try: d = vrdec.load(t)
        except Exception: continue
        n = sum(1 for k, (ti, b) in cellmap(d).items() if any(b))
        if best is None or n < best[0]: best = (n, t)
    return best[1] if best else None


def measure(dd, target, quiet, rom, name):
    vrdec.V = os.path.expanduser(dd)
    a, b = cellmap(vrdec.load(target)), cellmap(vrdec.load(quiet))
    diff = [k for k in a if a[k][1] != b[k][1]]
    if not diff:
        print("%-12s %s vs %s : 다른 칸 없음" % (name, target, quiet)); return None
    ys = [k[0] for k in diff]; xs = [k[1] for k in diff]
    r0, r1, c0, c1 = min(ys), max(ys), min(xs), max(xs)
    tiles = {a[k][0] for k in diff if any(a[k][1])}
    # 주소: 그 칸들이 롬 어디에 실렸나(유일한 것만 확실하다)
    addrs = []
    for k in sorted(diff):
        by = a[k][1]
        if not any(by): continue
        if rom.count(by) == 1: addrs.append(rom.find(by))
    span = ("0x%06X~0x%06X" % (min(addrs), max(addrs))) if addrs else "—"
    print("%-12s %s(바탕 %s) : **%d×%d칸 = %d×%d px** · 행 %d~%d 열 %d~%d · 다른 칸 %d · 타일종 %d · 지문 주소 %s"
          % (name, target, quiet, c1 - c0 + 1, r1 - r0 + 1, (c1 - c0 + 1) * 8, (r1 - r0 + 1) * 8,
             r0, r1, c0, c1, len(diff), len(tiles), span))
    return (r0, r1, c0, c1, len(tiles))
