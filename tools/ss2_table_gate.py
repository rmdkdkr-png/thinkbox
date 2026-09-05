# -*- coding: utf-8 -*-
"""SS2 포인터 표 관문 — 문자열 표 15칸(엔딩 JP/EN)·60칸(승리)·난입·싸움 전이 «문자열 시작»을 가리키는지 본다.
   이번 사고(v1.0 엔딩이 첫 쪽에서 멎음)의 재발 방지: 글을 옮기고 «한쪽 표만» 고치면 나머지 표가 채움(0xFF)이나
   글 한가운데를 가리켜, 어쩌다 맞은 편만 첫 쪽이 뜨고 둘째 쪽이 사라진다.
   판정: ① 목표가 롬 안 ② 목표 바이트가 0xFF(채움/종료)가 아님 ③ 목표 바로 앞이 종료(0xFF)이거나 표 구역 밖 — 즉 «시작»
   사용: python3 ss2_table_gate.py <롬…>"""
import os, sys

CPU = 0x200000
TABLES = [
    ('엔딩 JP', 0x05C98B, 15, 's16'),      # 부호 16비트 상대(기준 = 표 주소)
    ('엔딩 EN', 0x05C9A9, 15, 's16'),
    ('승리',    0x04E5F7, 164, 'u32'),     # CPU 절대(−0x200000)
]

def s16(b, a):
    v = b[a] | (b[a + 1] << 8)
    return v - 0x10000 if v >= 0x8000 else v

def targets(b, base, n, kind):
    out = []
    for i in range(n):
        if kind == 's16':
            out.append(base + s16(b, base + i * 2))
        else:
            a = base + i * 4
            out.append(int.from_bytes(b[a:a + 4], 'little') - CPU)
    return out

def check(path):
    b = open(path, 'rb').read()
    print('== %s (%d B)' % (os.path.basename(path), len(b)))
    bad_total = 0
    for ko, base, n, kind in TABLES:
        tg = targets(b, base, n, kind)
        oob = [t for t in tg if not (0 <= t < len(b) - 1)]
        fill = [t for t in tg if 0 <= t < len(b) and b[t] == 0xFF]
        mid = [t for t in tg if 0 < t < len(b) and b[t] != 0xFF and b[t - 1] not in (0xFF,)]
        uniq = len(set(tg))
        bad = len(oob) + len(fill)
        bad_total += bad
        print('   %-8s %3d칸 · 서로 다른 목표 %3d · 범위밖 %d · 채움(0xFF) %d · (참고) 앞이 종료 아님 %d'
              % (ko, n, uniq, len(oob), len(fill), len(mid)))
        if fill: print('      ⚠ 채움을 가리키는 칸: %s' % ['0x%06X' % t for t in fill[:6]])
    print('   판정:', '통과 ✓' if bad_total == 0 else '실패 ✗ (%d칸)' % bad_total)
    return bad_total == 0

ok = all(check(p) for p in sys.argv[1:])
sys.exit(0 if ok else 1)
