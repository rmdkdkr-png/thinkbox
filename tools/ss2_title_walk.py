# -*- coding: utf-8 -*-
"""제목 기록을 «렌더러처럼 순서대로 걸어» 120개가 제자리에 서는지 본다.
   문법: cnt16 | ptr32 | off16×cnt | 행수16 | 행마다 (타일색인… ff)"""
import io, os, sys, struct

def walk(path, base=0x07A7E4, n=120):
    d = io.open(os.path.expanduser(path), 'rb').read()
    p = base; out = []
    for i in range(n):
        st = p
        if p + 8 > len(d): out.append((i + 1, st, None, '롬 밖')); break
        cnt = struct.unpack_from('<H', d, p)[0]; p += 2
        ptr = struct.unpack_from('<I', d, p)[0]; p += 4
        if cnt > 64: out.append((i + 1, st, cnt, 'cnt 이상')); break
        offs = struct.unpack_from('<%dH' % cnt, d, p); p += 2 * cnt
        rows = struct.unpack_from('<H', d, p)[0]; p += 2
        if rows > 8: out.append((i + 1, st, cnt, 'rows 이상 %d' % rows)); break
        cells = []
        bad = False
        for r in range(rows):
            row = []
            while p < len(d) and d[p] != 0xFF:
                row.append(d[p]); p += 1
                if len(row) > 32: bad = True; break
            p += 1  # ff
            cells.append(row)
            if bad: break
        out.append((i + 1, st, cnt, 'ok' if not bad else '행 길이 이상',
                    ptr, rows, [len(c) for c in cells], p - st))
    return out, p

for path in sys.argv[1:]:
    rows, end = walk(path)
    ok = [r for r in rows if len(r) > 4 and r[3] == 'ok']
    print('== %s' % os.path.basename(path))
    print('   걸은 기록 %d개 · 끝 0x%06X' % (len(rows), end))
    if len(ok) != len(rows):
        for r in rows:
            if len(r) <= 4 or r[3] != 'ok':
                print('   ★ %d번째에서 걸림 @0x%06X : %s' % (r[0], r[1], r[3] if len(r) > 3 else r[-1]))
                break
    lens = sorted(set(r[7] for r in ok))
    print('   기록 길이 종류 %s' % lens[:8])
    cnts = sorted(set(r[2] for r in ok))
    print('   cnt 종류 %s · rows 종류 %s' % (cnts[:8], sorted(set(r[5] for r in ok))))
    cs = sorted(set(tuple(r[6]) for r in ok))
    print('   행 칸수 종류 %s' % cs[:6])
