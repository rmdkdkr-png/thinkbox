# -*- coding: utf-8 -*-
"""화면에서 잡아 둔 배너(p_*.json)와 롬 기록(표N)을 «타일 주소»로 맞춘다.

이름표를 믿지 않는다 — 주소가 겹치면 같은 것이고, 안 겹치면 아니다.
"""
import glob, json, os, struct, sys

ROM = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")
D = os.path.expanduser("~/ss2/repo/thinkbox/knowledge/gfx-ss2")
TB, BASE = 0x06F56D, 0x05F56D


def rec_tiles(rom, i):
    v = rom[TB + 2 * i] | (rom[TB + 2 * i + 1] << 8); a = BASE + v
    cnt = rom[a] | (rom[a + 1] << 8)
    base = struct.unpack("<I", rom[a + 2:a + 6])[0] - 0x200000
    o = a + 6
    off = [rom[o + 2 * j] | (rom[o + 2 * j + 1] << 8) for j in range(cnt)]
    return {base + v2 for v2 in off}


rom = open(ROM, "rb").read()
recs = {}
for i in range(48):
    try:
        recs[i] = rec_tiles(rom, i)
    except Exception:
        pass

# json 안에서 «주소처럼 보이는 정수»를 모조리 긁는다 — 구조를 모르니 통째로 본다
def nums(o, acc):
    if isinstance(o, dict):
        for v in o.values(): nums(v, acc)
    elif isinstance(o, list):
        for v in o: nums(v, acc)
    elif isinstance(o, int):
        acc.add(o)
    elif isinstance(o, str):
        try: acc.add(int(o, 16))
        except Exception: pass
    return acc


for f in sorted(glob.glob(os.path.join(D, "p_*.json"))):
    try:
        j = json.load(open(f))
    except Exception:
        continue
    got = nums(j, set())
    got = {v for v in got if 0x060000 <= v <= 0x070000}
    if not got:
        print("%-18s (롬 주소 없음)" % os.path.basename(f)); continue
    best = []
    for i, t in recs.items():
        n = len(got & t)
        if n: best.append((n, i))
    best.sort(reverse=True)
    print("%-18s 주소 %3d개 → %s" % (os.path.basename(f), len(got),
          ", ".join("표%d(%d/%d)" % (i, n, len(recs[i])) for n, i in best[:3]) or "겹치는 표 없음"))
