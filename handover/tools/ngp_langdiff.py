#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NGPC — «본체 언어 설정» 축으로 화면을 픽셀 대조한다.

## 왜 필요한가

NGPC 는 **게임 안에 언어 항목이 없다.** 본체(BIOS) 언어 설정을 게임이 읽고
(RAM `0x6F87`, 0=일본어 1=영어), 게임에 따라 **일본어판 글과 영어판 글을
아예 따로** 쓴다. 한패가 한쪽만 옮겼으면 다른 쪽에서는 원문이 그대로 나온다.

이걸 넉 판이나 모르고 냈다. 하네스가 `ngp_language` 기본값을 `japanese` 로
먹이고 있어서 **그 축을 한 번도 안 그렸기 때문**이다. 화면 검증은 전부
통과했는데, 통과한 이유가 「경우의 절반을 안 봤다」였다.

    「전부 통과」가 「전부 봤다」가 아니다.

## ★ 자부터 잰다 (안 그러면 가짜 통과가 나온다)

첫 판을 이 검사 없이 냈더니 본부가 바로 걸렸다 — **NGP_LANG 을 안 읽는
하네스**로 돌려서 두 판이 당연히 같았고, 「다름 0 = 통과」로 읽힐 뻔했다.
(같은 기계에 `ngprun` 이 여러 벌 있었고 그중 하나가 옛 빌드였다.)

그래서 이제 **먼저 자를 잰다** — 램 덤프에서 언어 바이트를 직접 읽어
일본어 판이 0, 영어 판이 1 인지 확인한다. 아니면 **결과를 아예 안 낸다.**

    램 덤프 오프셋 0x2F87  (= NGP RAM 0x6F87 − 0x4000)

## 쓰기

    ./ngp_langdiff.py <ngprun> <core.so> <롬> <대본> [작업폴더]

대본은 짧아도 된다. 여덟 게임을 가릴 때 쓴 것:

    600 / 2 B / 200 / !a / 2 ST / 200 / !b / 2 B / 250 / !c /
    2 B / 250 / !d / 2 D / 90 / 2 B / 250 / !e / 2 B / 250 / !f

## ★ 롬은 «순정» 으로 재라

작업 폴더에 굴러다니는 롬은 **이미 패치본인 경우가 많다.** 실제로 여덟 게임을
가릴 때 넷(svc·ss2·ms1·lb)이 순정이 아니었고, 그중 svc 는 옛 한패 0.172 본이었다.
결론은 우연히 맞았지만 방법이 틀렸다. `[!]` 덤프의 crc32 를 먼저 확인하라.

## 정상인데 다를 수도 있다

「다름」이 곧 결함은 아니다. 실제로 이런 것들이 나왔다:

    사무라이 쇼다운 1  난이도 표기가 「초급/중급/상급」↔「검객/검호/검성」
                     — 원문이 원래 다른 낱말이라 **양쪽 다 한글**이면 정상
    아랑전설 FC       타이틀 **로고 그림**만 다름 (FATAL FURY ↔ 餓狼伝説)
    사무라이 쇼다운 2  프롤로그 문장이 양쪽 다 한글 (일/영측 문장을 각각 옮김)

그러니 이 도구는 「볼 곳을 좁혀 주는 자」이지 판정기가 아니다. 다른 태그를
눈으로 열어 보고, **한쪽에 원문이 남아 있는지**를 사람이 본다.

## 고치는 법 (드러났을 때)

비교(`CP`, 읽기만)는 **건드리지 말고 분기만** 일본어 갈래로 고정한다.
`AND` 로 바꾸면 램에 되써서 **유저 본체 설정을 덮는다** — 쓰지 마라.

    JR  Z  (66) → JR  T (68)     JR  NZ (6E) → JR  F (60)
    JRL Z  (76) → JRL T (78)     JRL NZ (7E) → JRL F (70)
    JP  NZ (DE) → JP  F (D0)     RET Z (B0 F6) → RET T (B0 F8)
    RET NZ (B0 FE) → RET F (B0 F0)

게임이 부팅 때 한 번 읽어 제 변수에 캐시하는 꼴이면(KOF R-2 · SvC) 「영어
갈래가 싣는 상수」만 일본어 값으로 바꾸는 한 바이트로 끝난다.
"""
import os
import subprocess
import sys
import tempfile

LANG_OFF = 0x6F87 - 0x4000      # 램 덤프 안에서 언어 바이트가 있는 자리


def run(ngprun, core, rom, script, lang, prefix):
    env = dict(os.environ, NGP_LANG=lang)
    subprocess.run([ngprun, core, rom, script, prefix],
                   env=env, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=False)


def control(work):
    """자를 잰다 — 하네스가 설정을 정말 코어에 넘겼는가.

    램 덤프에서 언어 바이트를 직접 읽는다. 일본어 판이 0, 영어 판이 1 이
    아니면 이 판정은 **아무 뜻이 없다.**
    """
    for f in sorted(os.listdir(work)):
        if not (f.startswith('j_') and f.endswith('.ram')):
            continue
        g = os.path.join(work, 'e_' + f[2:])
        if not os.path.exists(g):
            continue
        j = open(os.path.join(work, f), 'rb').read()
        e = open(g, 'rb').read()
        if len(j) <= LANG_OFF or len(e) <= LANG_OFF:
            return None, '램 덤프가 너무 짧다'
        return (j[LANG_OFF], e[LANG_OFF]), None
    return None, '램 덤프가 없다 (대본에 !태그 가 있어야 한다)'


def main():
    a = sys.argv[1:]
    if len(a) < 4:
        print(__doc__)
        return 1
    ngprun, core, rom, script = a[:4]
    work = a[4] if len(a) > 4 else tempfile.mkdtemp(prefix='langdiff')
    os.makedirs(work, exist_ok=True)
    for lang in ('japanese', 'english'):
        run(ngprun, core, rom, script, lang, os.path.join(work, lang[0] + '_'))

    got, why = control(work)
    if got is None:
        print('  ✗ 자를 못 쟀다 — %s' % why)
        return 2
    if got != (0, 1):
        print('  ✗ 하네스가 NGP_LANG 을 안 넘긴다 (언어 바이트 %d/%d, 0/1 이어야 한다)'
              % got)
        print('    이 하네스로 잰 「다름 0」은 가짜다. ngprun 빌드를 확인하라.')
        return 2

    same, diff = 0, []
    for f in sorted(os.listdir(work)):
        if not (f.startswith('j_') and f.endswith('.ppm')):
            continue
        p, q = os.path.join(work, f), os.path.join(work, 'e_' + f[2:])
        if not os.path.exists(q):
            continue
        if open(p, 'rb').read() == open(q, 'rb').read():
            same += 1
        else:
            diff.append(f[2:-4])
    print('  %-26s 같음 %d · 다름 %d   %s'
          % (os.path.basename(rom), same, len(diff), diff))
    if diff:
        print('    → %s 에서 두 판을 열어 보라 (j_*.ppm / e_*.ppm).'
              ' **다름이 곧 결함은 아니다** — 한쪽에 원문이 남았는지를 보라.' % work)
    return 0


if __name__ == '__main__':
    sys.exit(main())
