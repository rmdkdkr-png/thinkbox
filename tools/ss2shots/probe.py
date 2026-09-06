# -*- coding: utf-8 -*-
"""«실리나»를 재는 유일하게 믿을 만한 법 — 표식을 박아 넣고 화면에 뜨는지 본다.

왜 이래야 하나: 「가리켜지나」도 「바이트가 보이나」도 답이 아니었다.
· 아이템이 가리키는 타일만 보면 **그 사이 빈 타일**을 놓친다(f7 의 첫 검사).
· 화면에 뜬 타일의 바이트를 롬에서 찾는 방식은 **빈 타일이 안 잡힌다**(내 검사).
둘 다 같은 병이다 — **참조가 없다고 비어 있는 것이 아니다.**

그래서 후보 대역을 **타일마다 다른 표식**으로 덮은 롬을 만들어 찍는다.
화면에 표식이 뜨면 그 주소는 «실리는» 자리다. 뜬 표식을 되짚으면 **어느 주소인지까지** 나온다.
"""
import os, struct, sys

SRC = os.path.expanduser("~/ss2/work_lang/v10/release_final/banners_v1.ngc")
OUT = os.path.expanduser("~/ss2/tmp/lb/probe.ngc")
LO, HI = 0x06D20D, 0x06F20D          # 재려는 대역
STEP = 16                            # 타일 하나


def tile(idx):
    """타일 하나 — 눈에 띄고, 되짚으면 색인이 나오게."""
    lo, hi = idx & 0xFF, (idx >> 8) & 0xFF
    return bytes([0xFF, 0xFF, lo, hi, 0xFF, 0xFF, lo, hi,
                  0xFF, 0xFF, lo, hi, 0xFF, 0xFF, lo, hi])


if __name__ == "__main__":
    b = bytearray(open(SRC, "rb").read())
    n = 0
    for a in range(LO, HI, STEP):
        b[a:a + STEP] = tile(n); n += 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "wb").write(bytes(b))
    print("%s · 0x%06X~0x%06X 를 표식 %d장으로 덮었다" % (OUT, LO, HI - 1, n))
