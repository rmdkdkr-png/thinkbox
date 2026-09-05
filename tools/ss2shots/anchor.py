# -*- coding: utf-8 -*-
"""배너 «밑자리» — 한 배너가 여러 덩이로 실릴 수 있으니 **덩이마다** 밑자리를 잡는다.

타일 색인이 이어지는 동안 롬 주소도 16씩 이어지면 한 덩이다. 끊기면 새 덩이로 센다.
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vrdec

ROM = os.path.expanduser("~/ss2/work_lang/v10/release_final/cards_v12_final.ngc")
JOBS = [
    ("~/ss2/tmp/vr",   "h_iza2",  range(5, 10), [10, 11, 12], "자아"),
    ("~/ss2/tmp/vr",   "h_iza2",  range(7, 15), [6, 7, 8], "당당히"),
    ("~/ss2/tmp/vr",   "h_iza3",  range(4, 15), [8, 9, 10, 11], "1회전"),
    ("~/ss2/tmp/vr23", "h_r2_16", range(4, 15), [8, 9, 10, 11], "2회전"),
    ("~/ss2/tmp/vr3r", "h_t12",   range(4, 15), [8, 9, 10, 11], "3회전"),
    ("~/ss2/tmp/vr23", "h_r2_00", range(4, 16), [7, 8, 9, 10, 11, 12], "승부"),
    ("~/ss2/tmp/vr23", "h_r2_07", range(5, 14), [8, 9, 10, 11], "한판!!"),
    ("~/ss2/tmp/vr23", "h_r3_07", range(5, 14), [8, 9, 10, 11], "완승"),
    ("~/ss2/tmp/vr23", "h_r2_13", range(5, 9),  range(5, 15), "승자 이름판"),
]

def run(rom, dd, tag, rows, cols, name):
    vrdec.V = os.path.expanduser(dd); d = vrdec.load(tag)
    idx = sorted({vrdec.cell(d["scroll"], 0, r, c)[0] for r in rows for c in cols})
    # 타일마다 «롬에서 나올 수 있는 자리» 전부
    cand = {}
    for t in idx:
        b = d["char"][t*16:t*16+16]
        if not any(b): continue
        p, w = [], -1
        while True:
            w = rom.find(b, w+1)
            if w < 0: break
            p.append(w)
        cand[t] = p
    # 덩이 나누기: 색인 순서대로 훑으며 «앞 타일 주소+16» 이 후보에 있으면 같은 덩이
    ks = sorted(cand); groups = []; cur = None
    for t in ks:
        if cur is not None:
            want = cur[-1][1] + (t - cur[-1][0]) * 16
            if want in cand[t]: cur.append((t, want)); continue
            groups.append(cur)
        # 새 덩이 — 유일한 자리를 먼저, 없으면 첫 자리
        u = [a for a in cand[t] if len(cand[t]) == 1]
        cur = [(t, (u or cand[t])[0])]
    if cur: groups.append(cur)
    print("%s — 타일 %d장 · 덩이 %d개" % (name, len(cand), len(groups)))
    for g in groups:
        A = g[0][1] - g[0][0] * 16
        ok = sum(1 for t, a in g if rom[a:a+16] == d["char"][t*16:t*16+16])
        print("   밑자리 0x%06X · 타일 %d~%d (%d장) · 첫 0x%06X · 끝 0x%06X · 검산 %d/%d"
              % (A, g[0][0], g[-1][0], len(g), g[0][1], g[-1][1], ok, len(g)))

if __name__ == "__main__":
    rom = open(ROM, "rb").read()
    for j in JOBS: run(rom, *j)
