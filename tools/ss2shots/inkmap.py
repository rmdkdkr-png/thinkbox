# -*- coding: utf-8 -*-
"""시안·화면·어긋난 자리를 세 폭으로 그린다 — 「어디가 다른가」를 눈으로 짚는다.

색이 서로 다른 체계(시안은 흰·회색, 화면은 붉은색)라 나란히 놓아도 눈으로는 못 견준다.
그래서 **잉크냐 아니냐**로 바꿔 그린다: 잉크는 검정, 바탕은 흰색, 어긋난 자리는 빨강.
"""
import collections, os, struct, sys, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artdiff import readpng, screen_crop

TRANS = (0, 0, 0)


def png(path, W, H, rows):
    ck = lambda tg, d: struct.pack(">I", len(d)) + tg + d + struct.pack(">I", zlib.crc32(tg + d) & 0xffffffff)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n"
                           + ck(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
                           + ck(b"IDAT", zlib.compress(bytes(rows), 9)) + ck(b"IEND", b""))


def run(art, ppm, x0, y0, out, S=4):
    W, H, a = readpng(os.path.expanduser(art))
    s = screen_crop(os.path.expanduser(ppm), x0, y0, W, H)
    pair = collections.defaultdict(collections.Counter)
    for i in range(len(a)):
        if a[i] != TRANS: pair[a[i]][s[i]] += 1
    m = {c: cc.most_common(1)[0][0] for c, cc in pair.items()}
    ink = set(m.values())
    BLACK, WHITE, RED, GREY = b"\x00\x00\x00", b"\xff\xff\xff", b"\xe0\x00\x00", b"\xc8\xc8\xc8"
    GAP, PW = 8, W * 3 + 8 * 2
    rows = bytearray()
    for y in range(H):
        line = bytearray()
        for panel in range(3):
            for x in range(W):
                i = y * W + x
                want, got = a[i] != TRANS, s[i] in ink
                if panel == 0: px = BLACK if want else WHITE
                elif panel == 1: px = BLACK if got else WHITE
                else:
                    bad = (want != got) or (want and s[i] != m[a[i]])
                    px = RED if bad else (GREY if want else WHITE)
                line += px * S
            if panel < 2: line += b"\x60\x60\x60" * (GAP * S)
        for _ in range(S): rows += b"\x00" + bytes(line)
    png(out, PW * S, H * S, rows)
    # 칸별 어긋남
    bad = collections.Counter()
    for i in range(len(a)):
        want, got = a[i] != TRANS, s[i] in ink
        if want != got or (want and s[i] != m[a[i]]):
            bad[((i // W) // 8, (i % W) // 8)] += 1
    return out, bad


if __name__ == "__main__":
    out, bad = run(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    print(out, "· 왼쪽=시안 가운데=화면 오른쪽=어긋난 자리(빨강)")
    for (cy, cx), n in sorted(bad.items(), key=lambda kv: -kv[1]):
        print("   행%d 열%d — %d/64" % (cy, cx, n))
