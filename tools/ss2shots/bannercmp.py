# -*- coding: utf-8 -*-
"""배너를 «태그»가 아니라 «내용»으로 짝지어 두 롬을 견준다.

롬이 다르면 같은 대본도 다른 순간에 닿는다(traps ⑬). 그래서 태그로 짝지으면
「무너졌다」로 오판한다 — 실제로 한 번 그럴 뻔했다.
그러니 롬마다 **그 배너가 제일 많이 뜬 프레임**을 따로 고른 뒤 그 둘을 견준다.
"""
import glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vrdec

REG = {"자아":   (0x06C020, 0x06C110),
       "당당히": (0x07EC60, 0x07EDF0),
       "회전":   (0x06C2A0, 0x06C5E0),
       "한판!!": (0x06CDD0, 0x06CF90),
       "완승":   (0x06CFB0, 0x06D160),
       "이름판": (0x1E52C0, 0x1E5640),
       "승부":   (0x06CB40, 0x06F560)}


def best(dump, rom, lo, hi):
    """그 배너가 제일 많이 뜬 프레임과 그 칸 지도."""
    seg = rom[lo:hi]; vrdec.V = dump; top = None
    for f in sorted(glob.glob(dump + "/*.scroll")):
        t = os.path.basename(f).rsplit(".", 1)[0]
        try: d = vrdec.load(t)
        except Exception: continue
        m = {}
        for r in range(19):
            for c in range(20):
                ti = vrdec.cell(d["scroll"], 0, r, c)[0]
                b = d["char"][ti * 16:ti * 16 + 16]
                if not any(b) or rom.count(b) > 1: continue
                if seg.find(b) >= 0: m[(r, c)] = b
        if top is None or len(m) > len(top[1]): top = (t, m)
    return top


if __name__ == "__main__":
    A = os.path.expanduser("~/ss2/tmp/vrALL"); RA = open(os.path.expanduser(
        "~/ss2/work_lang/v10/release_final/banners_v1.ngc"), "rb").read()
    L = os.path.expanduser("~/ss2/tmp/vrLEN"); RL = open(os.path.expanduser(
        "~/ss2/work_lang/v10/release_final/test_lenchg.ngc"), "rb").read()
    for name, (lo, hi) in REG.items():
        ta, ma = best(A, RA, lo, hi)
        tb, mb = best(L, RL, lo, hi)
        only_a = sorted(set(ma) - set(mb)); only_b = sorted(set(mb) - set(ma))
        diff = [k for k in set(ma) & set(mb) if ma[k] != mb[k]]
        v = "같다" if not (only_a or only_b or diff) else \
            "**바탕에만 %d칸 · 시험에만 %d칸 · 그림 다른 칸 %d개**" % (len(only_a), len(only_b), len(diff))
        print("%-7s 바탕 %s(%d칸) · 시험 %s(%d칸) → %s" % (name, ta, len(ma), tb, len(mb), v))
        for k in only_a[:4]: print("      바탕에만 행%d 열%d" % k)
        for k in only_b[:4]: print("      시험에만 행%d 열%d" % k)
