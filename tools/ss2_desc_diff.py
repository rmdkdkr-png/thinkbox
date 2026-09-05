# -*- coding: utf-8 -*-
"""카드 설명 — «손댄 카드만 달라졌나»를 바이트로 본다.
   글자가 «깨진 것»이 아니라 «멀쩡한 다른 글자»로 바뀌면 화면 판정기에 안 걸린다.
   그래서 배포본과 견줘, 고치기로 한 카드 말고 달라진 것이 있으면 잡는다."""
import io, os, sys, struct

R = os.path.expanduser('~/ss2/work_lang/v10/release_final/')
BASE = R + 'ss2_v1.0_final.ngc'
CAND = os.path.expanduser(sys.argv[1]) if len(sys.argv) > 1 else R + 'cards_v10_final.ngc'
EDITED = set(int(x) for x in (sys.argv[2].split(',') if len(sys.argv) > 2 else
                              ['22', '28', '63', '66', '112', '115', '120']))

STR_TBL = 0x0319EB          # u16 × 120, 표머리 기준
LIST_TBL = 0x1EF5A0         # u32 × 121 (CPU)

def strings(d):
    out = []
    for i in range(120):
        off = struct.unpack_from('<H', d, STR_TBL + 2 * i)[0]
        a = STR_TBL + off
        e = a
        while d[e] != 0xFF: e += 1
        out.append(d[a:e + 1])
    return out

def lists(d):
    out = []
    for i in range(121):
        p = struct.unpack_from('<I', d, LIST_TBL + 4 * i)[0] - 0x200000
        n = d[p]
        out.append((p, d[p:p + 1 + 2 * n]))
    return out

a = io.open(BASE, 'rb').read()
b = io.open(CAND, 'rb').read()
sa, sb = strings(a), strings(b)
la, lb = lists(a), lists(b)

print('후보 %s' % os.path.basename(CAND))
print('고치기로 한 카드: %s' % sorted(EDITED))
print('-' * 70)
ds = [i + 1 for i in range(120) if sa[i] != sb[i]]
dl = [i + 1 for i in range(120) if la[i][1] != lb[i][1]]
print('글월이 달라진 카드   %2d장  %s' % (len(ds), ds))
print('글자 목록이 달라진 카드 %2d장  %s' % (len(dl), dl))
print('-' * 70)
bad_s = [x for x in ds if x not in EDITED]
bad_l = [x for x in dl if x not in EDITED]
half = sorted(set(ds) ^ set(dl))
ok = True
if bad_s: ok = False; print('✘ 안 고치기로 한 카드의 글월이 달라졌다: %s' % bad_s)
if bad_l: ok = False; print('✘ 안 고치기로 한 카드의 목록이 달라졌다: %s' % bad_l)
if half:
    ok = False
    print('✘ ★글월과 목록이 «짝이 안 맞게» 달라진 카드: %s' % half)
    print('   — 한쪽만 바뀌면 화면에 «멀쩡한 다른 글자»가 뜬다. 깨짐 판정기에 안 걸린다.')
for n in sorted(EDITED):
    i = n - 1
    print('   %3d  글월 %s · 목록 %s · 목록자리 0x%06X→0x%06X' % (
        n, '바뀜' if sa[i] != sb[i] else '그대로',
        '바뀜' if la[i][1] != lb[i][1] else '그대로', la[i][0], lb[i][0]))
print('-' * 70)
print('판정 %s' % ('✔ 손댄 카드만, 글월·목록이 짝으로 달라졌다' if ok else '★불합격'))
