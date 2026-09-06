# -*- coding: utf-8 -*-
"""그림 글자 48개를 롬에서 «세워 그린다» — 에뮬레이터가 필요 없다.

왜 이렇게 하나: 화면을 찾아다니면 「어느 순간에 뜨나」만 알게 된다.
발주에 필요한 것은 **「무엇이라 쓰여 있나」**이고, 그건 그려 보면 읽힌다.

문법: cnt16 | ptr32 | off16×cnt | 행수16 | 행마다 «타일 색인» … ff
  · 타일 주소 = (ptr − 0x200000) + off[색인]
  · 각 행의 첫 칸은 **암묵**이다(색인 0) — 명시된 칸 앞에 하나 더 있다
  · 타일 16바이트 = 8줄 × 2바이트, 한 줄 8화소가 2비트씩
"""
import os, struct, sys, zlib

ROM = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")
OUT = os.path.expanduser("~/ss2/tmp/items")
TB, BASE = 0x06F56D, 0x05F56D
# 읽기용 색: 0 투명(자홍 바탕) · 1 밝은 · 2 중간 · 3 어두운
PAL = [(255, 0, 255), (255, 255, 255), (150, 150, 150), (40, 40, 40)]


def tile(rom, a):
    out = []
    for y in range(8):
        w = (rom[a + y * 2] << 8) | rom[a + y * 2 + 1]
        out.append([(w >> (14 - 2 * x)) & 3 for x in range(8)])
    return out


def record(rom, i):
    v = rom[TB + 2 * i] | (rom[TB + 2 * i + 1] << 8); a = BASE + v
    cnt = rom[a] | (rom[a + 1] << 8)
    ptr = struct.unpack("<I", rom[a + 2:a + 6])[0]
    base = ptr - 0x200000 if ptr >= 0x200000 else ptr
    o = a + 6
    off = [rom[o + 2 * j] | (rom[o + 2 * j + 1] << 8) for j in range(cnt)]
    p = o + 2 * cnt
    nrow = rom[p] | (rom[p + 1] << 8); p += 2
    rows = []
    for _ in range(nrow):
        L = []
        while rom[p] != 0xFF: L.append(rom[p]); p += 1
        p += 1
        # ★ 암묵 첫 칸은 «빈 칸»이다 — 색인 0 이 아니다.
        #   색인 0 으로 두면 왼쪽에 같은 조각이 줄줄이 반복돼 글자가 안 읽힌다.
        #   대조군으로 갈랐다: 표17 은 빈 칸으로 둘 때만 「一本!!」로 읽힌다.
        rows.append([None] + L)
    return a, base, off, rows


def png(path, W, H, px, S=1):
    raw = bytearray()
    for y in range(H):
        line = bytearray()
        for x in range(W): line += bytes(px[y * W + x]) * S
        for _ in range(S): raw += b"\x00" + bytes(line)
    ck = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n"
                           + ck(b"IHDR", struct.pack(">IIBBBBB", W * S, H * S, 8, 2, 0, 0, 0))
                           + ck(b"IDAT", zlib.compress(bytes(raw), 9)) + ck(b"IEND", b""))


def draw(rom, i):
    a, base, off, rows = record(rom, i)
    w = max(len(r) for r in rows); h = len(rows)
    W, H = w * 8, h * 8
    px = [PAL[0]] * (W * H)
    cells = []
    for ry, r in enumerate(rows):
        for cx, idx in enumerate(r):
            if idx is None or idx >= len(off): continue
            ta = base + off[idx]
            cells.append((ry, cx, ta))
            if ta + 16 > len(rom): continue
            t = tile(rom, ta)
            for y in range(8):
                for x in range(8):
                    px[(ry * 8 + y) * W + cx * 8 + x] = PAL[t[y][x]]
    return a, W, H, px, cells


if __name__ == "__main__":
    rom = open(ROM, "rb").read()
    os.makedirs(OUT, exist_ok=True)
    which = [int(x) for x in sys.argv[1:]] or list(range(48))
    tsv = []
    for i in which:
        try: a, W, H, px, cells = draw(rom, i)
        except Exception as e: print("표%d 못 그림 (%s)" % (i, e)); continue
        png("%s/%02d_1x.png" % (OUT, i), W, H, px, 1)
        png("%s/%02d_4x.png" % (OUT, i), W, H, px, 4)
        print("표%2d 0x%06X · %d×%d칸 %d×%d px · 칸 %d개" % (i, a, W // 8, H // 8, W, H, len(cells)))
        for ry, cx, ta in cells: tsv.append("%d\t0x%06X\t%d\t%d\t0x%06X" % (i, a, ry, cx, ta))
    open("%s/cellmap.tsv" % OUT, "w").write("표\t기록주소\t행\t칸\t타일주소\n" + "\n".join(tsv) + "\n")
    print("칸 지도 → %s/cellmap.tsv (%d줄)" % (OUT, len(tsv)))
