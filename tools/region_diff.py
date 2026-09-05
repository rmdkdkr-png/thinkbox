# -*- coding: utf-8 -*-
"""배포판이 «선언한 자리 밖»을 덮었는지 본다.
   쓴 것을 확인하는 관문은 덮은 것을 못 본다 — 그래서 바이트 차분을 구역으로 갈라 본다."""
import io, os, sys

BASE = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '~/ss2/work_lang/v10/release_final/ss2_v1.0_final.ngc')
NEW  = os.path.expanduser(sys.argv[2] if len(sys.argv) > 2 else '~/ss2/work_lang/v10/release_final/cards_v2.ngc')

# 카드 작업이 «쓴다고 선언한» 자리 (cards-plan / space-and-scope 기준)
DECLARED = [
    (0x031ADB, 0x033ED8, '카드 설명 문자열'),
    (0x0319EB, 0x031ADB, '카드 설명 문자열 표'),
    (0x07A7E4, 0x07C643, '제목 기록 표'),
    (0x07C643, 0x07E562, '제목 타일(순정 자리)'),
    (0x07E562, 0x07F031, '풀 꼬리 A'),
    (0x07F390, 0x0822FB, '풀 꼬리 B(순정 제목 타일이던 곳)'),
    (0x1E7C00, 0x1EA5F3, '카드 글꼴 뭉치'),
    (0x1EA5F3, 0x1EBB20, '카드 기술자'),
    (0x1EBB20, 0x1ED74D, '회수 구역'),
    (0x1ED940, 0x1EF4E9, '카드 글자 목록'),
    (0x1EF4E9, 0x1EF800, '목록 표·즉값'),
]

a = io.open(BASE, 'rb').read()
b = io.open(NEW, 'rb').read()
assert len(a) == len(b), '길이가 다르다'

# 바뀐 바이트를 이어진 덩어리로 모은다
runs, s = [], None
for i in range(len(a)):
    if a[i] != b[i]:
        if s is None: s = i
    elif s is not None:
        runs.append((s, i)); s = None
if s is not None: runs.append((s, len(a)))

def where(x):
    for lo, hi, ko in DECLARED:
        if lo <= x < hi: return ko
    return None

tot = sum(e - s for s, e in runs)
print('바뀐 바이트 %d개 · 덩어리 %d개' % (tot, len(runs)))
print('-' * 68)
inside, outside = 0, []
for s, e in runs:
    ko = where(s)
    if ko and where(e - 1) == ko:
        inside += e - s
    else:
        outside.append((s, e))
for lo, hi, ko in DECLARED:
    n = sum(min(e, hi) - max(s, lo) for s, e in runs if s < hi and e > lo)
    if n: print('선언 안  0x%06X~0x%06X  %-24s %7d B' % (lo, hi, ko, n))
print('-' * 68)
if not outside:
    print('★ 선언한 자리 밖은 0 바이트 — 덮은 것 없다')
else:
    n = sum(e - s for s, e in outside)
    print('★★ 선언 밖 %d 바이트 · 덩어리 %d개' % (n, len(outside)))
    for s, e in outside[:20]:
        print('   0x%06X~0x%06X  %6d B   (%s)' % (s, e, e - s, where(s) or '선언 없음'))
    if len(outside) > 20: print('   … %d개 더' % (len(outside) - 20))
