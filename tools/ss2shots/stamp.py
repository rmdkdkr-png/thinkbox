# -*- coding: utf-8 -*-
"""검사기가 «무엇을 쟀는지»를 먼저 찍는다 — 파일 이름 · md5 · 크기 · 고친 때.

왜 필요한가: 승부가 실기에서 안 읽힌 소동의 뿌리가 이것이었다.
한쪽은 **옛 그림(v1.0)**을 재고, 한쪽은 **추출기 JSON**을 재고, 나는 **시안과 화면**만 봤다.
셋 다 「내가 잰 것」을 안 적었으니 서로 다른 것을 재면서 같은 말을 하는 줄 알았다.

→ 어떤 판정이든 **그 판정이 무엇을 근거로 했는지**를 같이 남긴다.
"""
import hashlib, os, time


def of(path, label=""):
    p = os.path.expanduser(path)
    try:
        b = open(p, "rb").read()
        h = hashlib.md5(b).hexdigest()[:12]
        t = time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(p)))
        return "  %s%s · %d B · md5 %s · %s" % ((label + " ") if label else "", p, len(b), h, t)
    except Exception as e:
        return "  %s%s · **못 읽음** (%s)" % ((label + " ") if label else "", p, e)


def head(title, **files):
    """검사 머리말 — 무엇을 무엇과 견줬는지."""
    print("=== %s" % title)
    for k, v in files.items():
        print(of(v, "[%s]" % k))
    print("---")


if __name__ == "__main__":
    import sys
    head("보기", **{"롬": sys.argv[1] if len(sys.argv) > 1 else "~/ss2/work_lang/v10/release_final/banners_v3.ngc"})
