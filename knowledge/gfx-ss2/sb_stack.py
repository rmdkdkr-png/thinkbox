# -*- coding: utf-8 -*-
"""「승부」 열두 조각을 «세로로» 이어 붙여 본다.

가설: 표13·14·38~47 은 각각 1행×6칸(48×8px)이고, 열둘을 쌓으면 48×96 —
내가 앞서 화면에서 잰 「승부」 크기와 정확히 같다. 순서가 맞는지 **눈으로** 가른다.
맞으면 조립 좌표는 «표 번호 순서대로 8px 씩 아래»가 된다.
"""
import os, struct, sys, zlib

ROM = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")
TB, BASE = 0x06F56D, 0x05F56D
PAL = [(255, 255, 255), (0, 0, 0), (110, 110, 110), (60, 60, 60)]
ORDER = [13, 14] + list(range(38, 48))


def rec(rom, i):
    v = rom[TB + 2 * i] | (rom[TB + 2 * i + 1] << 8); a = BASE + v
    cnt = rom[a] | (rom[a + 1] << 8)
    ptr = struct.unpack("<I", rom[a + 2:a + 6])[0]
    base = ptr - 0x200000
    o = a + 6
    off = [rom[o + 2 * j] | (rom[o + 2 * j + 1] << 8) for j in range(cnt)]
    p = o + 2 * cnt
    nrow = rom[p] | (rom[p + 1] << 8); p += 2
    rows = []
    for _ in range(nrow):
        L = []
        while rom[p] != 0xFF: L.append(rom[p]); p += 1
        p += 1
        rows.append([None] + L)
    return base, off, rows


def tile(rom, a):
    return [[((((rom[a + y * 2] << 8) | rom[a + y * 2 + 1]) >> (14 - 2 * x)) & 3)
             for x in range(8)] for y in range(8)]


def png(path, W, H, px, S):
    raw = bytearray()
    for y in range(H):
        line = bytearray()
        for x in range(W): line += bytes(px[y * W + x]) * S
        for _ in range(S): raw += b"\x00" + bytes(line)
    ck = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n"
                           + ck(b"IHDR", struct.pack(">IIBBBBB", W * S, H * S, 8, 2, 0, 0, 0))
                           + ck(b"IDAT", zlib.compress(bytes(raw), 9)) + ck(b"IEND", b""))


rom = open(ROM, "rb").read()
W, H = 48, 8 * len(ORDER)
px = [PAL[0]] * (W * H)
lines = []
for k, i in enumerate(ORDER):
    base, off, rows = rec(rom, i)
    r = rows[0]
    lines.append("표%2d 칸→타일: %s" % (i, " ".join(
        "빈" if c is None else "0x%06X" % (base + off[c]) for c in r)))
    for cx, idx in enumerate(r):
        if idx is None or idx >= len(off): continue
        t = tile(rom, base + off[idx])
        for y in range(8):
            for x in range(8):
                if cx * 8 + x < W:
                    px[(k * 8 + y) * W + cx * 8 + x] = PAL[t[y][x]]
out = os.path.expanduser("~/ss2/tmp/items/sb_stack.png")
png(out, W, H, px, 10)
print("\n".join(lines))
print("→", out, "(%dx%d, 10배)" % (W, H))
