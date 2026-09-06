# -*- coding: utf-8 -*-
"""1-e8 의 물음에 «기록에서 뽑아» 답한다. 짐작으로 안 채운다.

① 칸 마스크 해석이 맞나 — 행마다 첫 칸 + 0행이 한 칸 짧은가?
② 팔레트 — 기록 안에 팔레트 바이트가 «있는가»?
③ 「승부」 조각들의 크기와 구조
"""
import os, struct, sys

ROM = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")
TB, BASE = 0x06F56D, 0x05F56D


def record(rom, i):
    v = rom[TB + 2 * i] | (rom[TB + 2 * i + 1] << 8)
    a = BASE + v
    cnt = rom[a] | (rom[a + 1] << 8)
    ptr = struct.unpack("<I", rom[a + 2:a + 6])[0]
    o = a + 6
    off = [rom[o + 2 * j] | (rom[o + 2 * j + 1] << 8) for j in range(cnt)]
    p = o + 2 * cnt
    nrow = rom[p] | (rom[p + 1] << 8)
    p += 2
    rows = []
    for _ in range(nrow):
        L = []
        while rom[p] != 0xFF:
            L.append(rom[p]); p += 1
        p += 1
        rows.append(L)
    return a, cnt, ptr, off, rows, p


rom = open(ROM, "rb").read()

print("=" * 66)
print("① 행별 «명시된 칸 수» — 0행이 정말 한 칸 짧은가")
print("=" * 66)
bad = []
for i in range(48):
    try:
        a, cnt, ptr, off, rows, end = record(rom, i)
    except Exception:
        continue
    ns = [len(r) for r in rows]
    if not ns:
        continue
    rest = set(ns[1:])
    tag = ""
    if len(rest) == 1 and ns[0] == list(rest)[0] - 1:
        tag = "0행이 한 칸 짧다 ✔"
    elif len(rest) == 1 and ns[0] == list(rest)[0]:
        tag = "모든 행이 같다"
    else:
        tag = "행마다 다르다"
        bad.append(i)
    print("표%2d  행수 %2d  칸수 %s   %s"
          % (i, len(rows), ("%d + %s" % (ns[0], sorted(rest))) if rest else str(ns), tag))

print()
print("=" * 66)
print("② 기록 안에 «팔레트 바이트»가 있는가 — 기록을 통째로 덤프해 확인")
print("=" * 66)
for i in (16, 17):
    a, cnt, ptr, off, rows, end = record(rom, i)
    print("표%d  기록 0x%06X~0x%06X (%d바이트)" % (i, a, end, end - a))
    print("   머리: cnt=%d  ptr=0x%08X  (타일밑자리 0x%06X)" % (cnt, ptr, ptr - 0x200000))
    print("   off[%d] = %s%s" % (len(off), ["0x%X" % v for v in off[:8]],
                                 " …" if len(off) > 8 else ""))
    print("   행 %d개, 첫 행 = %s" % (len(rows), rows[0]))
    print("   기록 원시바이트: %s" % rom[a:end].hex())
    print()

print("=" * 66)
print("③ 「승부」 계통 — 표13·14 와 38~47 의 생김새")
print("=" * 66)
for i in [13, 14] + list(range(38, 48)):
    try:
        a, cnt, ptr, off, rows, end = record(rom, i)
    except Exception as e:
        print("표%2d  못 읽음 (%s)" % (i, e)); continue
    w = max(len(r) for r in rows) + 1        # 암묵 첫 칸 포함
    print("표%2d  0x%06X  %d행×%d칸 = %d×%dpx  타일밑자리 0x%06X  칸 %d개"
          % (i, a, len(rows), w, w * 8, len(rows) * 8, ptr - 0x200000, cnt))
