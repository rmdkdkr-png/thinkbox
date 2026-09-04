#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NGPC — 패치가 «본체(BIOS) 설정 램» 을 건드리는지 실제로 돌려서 잡는다.

## 왜 필요한가 — 화면으로는 영영 안 보이는 결함

v0.5 에서 언어 검사를 `CP`(읽기 전용) 에서 `AND`(읽기-수정-쓰기) 로 바꿔 놓고
「그 자리가 0 이 되니 한 번만 지나가면 끝」이라며 **되쓰기를 이점으로 릴리즈
본문에 적기까지 했다.** `0x6F87` 은 **유저 본체의 언어 설정 램**이다.

에뮬레이터는 켤 때마다 램이 새것이라 아무 표도 안 난다. 화면 54장 픽셀 대조도
통과했다. 그런데 실기에서 그 영역이 배터리 백업이면 **유저 본체 설정이 실제로
바뀌고, 되돌리기도 어렵다.**

    「화면이 같다」는 이 축의 증거가 아니다.

정적 검사(그 주소를 목적지로 삼는 명령이 0곳인가)는 이미 빌드에 있다. 이 도구는
**동적으로** — 실제로 돌려서 그 바이트가 살아남는지 — 본다. 둘은 서로를 대신하지
못한다. 정적 검사는 «내가 아는 명령 형태» 만 보고, 동적 검사는 «지나간 길» 만 본다.

## ★ 스스로 반응하는지부터 증명한다

이 도구는 결과를 내기 전에 **일부러 고장을 심은 판을 한 번 더 돌린다.**
그 판에서 「망가졌다」가 안 나오면 **도구가 고장난 것**이므로 아무 결과도 안 낸다.

    「게임이 안 건드린다」와 「도구가 못 본다」가 똑같이 «통과» 로 나온다.
    결과만 봐서는 구분이 안 되니, 도구가 제 자를 스스로 재게 한다.

앞서 언어 축 대조 도구를 이 검사 없이 넘겼다가 가짜 통과가 날 뻔했다.

## 쓰기

    ./ngp_settings_guard.py <ngprun> <core.so> <롬> <대본> [작업폴더]

대본에 `!태그` 가 하나 이상 있어야 한다 (램 덤프가 거기서 나온다).
코어가 램을 안 내주면(RACE 등) 이 도구는 못 쓴다 — 그것도 말해 준다.
"""
import os
import shutil
import subprocess
import sys
import tempfile

LANG_ADDR = 0x6F87              # NGP 램 안 본체 언어 설정
LANG_OFF = LANG_ADDR - 0x4000   # 램 덤프 안에서의 자리
WANT = {'japanese': 0, 'english': 1}


def run(ngprun, core, rom, script, lang, prefix):
    subprocess.run([ngprun, core, rom, script, prefix],
                   env=dict(os.environ, NGP_LANG=lang),
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   check=False)


def survey(work, prefix, want):
    """램 덤프를 전부 열어 언어 바이트가 살아 있는지 본다.

    돌려주는 것: (덤프 수, 망가진 태그 목록, 못 잰 이유)
    """
    d, base = os.path.dirname(prefix) or '.', os.path.basename(prefix)
    dumps = sorted(f for f in os.listdir(d)
                   if f.startswith(base) and f.endswith('.ram'))
    if not dumps:
        return 0, [], '램 덤프가 없다 (대본에 !태그 를 넣어라)'
    bad = []
    seen = 0
    for f in dumps:
        b = open(os.path.join(d, f), 'rb').read()
        if len(b) <= LANG_OFF:
            return 0, [], ('코어가 램을 안 내준다 (덤프 %d바이트) — 이 코어로는'
                           ' 못 잰다' % len(b))
        seen += 1
        if b[LANG_OFF] != want:
            bad.append((f[len(base):-4], b[LANG_OFF]))
    return seen, bad, None


def one(ngprun, core, rom, script, work, tag, extra_poke=None):
    """한 판 — 필요하면 대본 끝에 고장을 심어서 돌린다."""
    scr = script
    if extra_poke is not None:
        scr = os.path.join(work, 'inject.txt')
        with open(scr, 'w', encoding='utf-8') as fp:
            fp.write('!poke %X=%d\n' % (LANG_OFF, extra_poke))
            fp.write(open(script, encoding='utf-8').read())
    out = {}
    for lang, want in WANT.items():
        pre = os.path.join(work, '%s_%s_' % (tag, lang[0]))
        run(ngprun, core, rom, scr, lang, pre)
        out[lang] = survey(work, pre, want)
    return out


def main():
    a = sys.argv[1:]
    if len(a) < 4:
        print(__doc__)
        return 1
    ngprun, core, rom, script = a[:4]
    work = a[4] if len(a) > 4 else tempfile.mkdtemp(prefix='setguard')
    os.makedirs(work, exist_ok=True)

    # ── ① 자를 먼저 잰다 — 일부러 0 으로 덮어쓰는 판을 돌린다.
    #     english 판은 1 이어야 하는데 0 으로 눌렸으니 «망가졌다» 가 나와야 한다.
    cal = one(ngprun, core, rom, script, work, 'cal', extra_poke=0)
    seen, bad, why = cal['english']
    if why:
        print('  ✗ 잴 수가 없다 — %s' % why)
        return 2
    if not bad:
        print('  ✗ 도구가 고장났다 — 일부러 0 으로 덮었는데 못 잡았다.')
        print('    이 도구로 낸 「통과」는 가짜다. poke 나 램 오프셋을 확인하라.')
        return 2
    print('  자가 검사 통과 — 심은 고장 %d/%d 덤프에서 잡힘' % (len(bad), seen))

    # ── ② 진짜 판
    res = one(ngprun, core, rom, script, work, 'run')
    ok = True
    for lang in ('japanese', 'english'):
        seen, bad, why = res[lang]
        if why:
            print('  ✗ %-9s 못 쟀다 — %s' % (lang, why))
            ok = False
        elif bad:
            ok = False
            print('  ✗ %-9s 본체 설정이 **망가졌다** — 덤프 %d개 중 %d개'
                  % (lang, seen, len(bad)))
            for t, v in bad[:6]:
                print('       %-10s 0x6F87 = %d (%d 이어야 한다)'
                      % (t, v, WANT[lang]))
        else:
            print('  ✓ %-9s 덤프 %d개 전부 0x6F87 = %d 그대로'
                  % (lang, seen, WANT[lang]))
    if ok:
        print('  → 패치는 본체 설정 램을 건드리지 않는다.')
    if not sys.argv[5:]:
        shutil.rmtree(work, ignore_errors=True)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
