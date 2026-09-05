# -*- coding: utf-8 -*-
"""배포 후보 관문 — 본부 몫. 이식소 화면 검사와 별개로 롬만 보고 거는 것."""
import io, os, struct, hashlib

R = os.path.expanduser('~/ss2/work_lang/v10/release_final/')
BASE = R + 'ss2_v1.0_final.ngc'
CAND = R + 'cards_v5.ngc'
PRIS = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")

a = io.open(BASE, 'rb').read()
b = io.open(CAND, 'rb').read()
pr = io.open(PRIS, 'rb').read()
ok = True
def chk(cond, ko, extra=''):
    global ok
    if not cond: ok = False
    print('%s %s %s' % ('✔' if cond else '✘', ko, extra))

print('후보 %s  md5 %s' % (os.path.basename(CAND), hashlib.md5(b).hexdigest()))
print('-' * 66)

chk(len(b) == 2097152, '길이 2,097,152 B', '(%d)' % len(b))

# ① 세이브 구역을 안 건드렸나 (SS2 는 0x1F0200~)
n = sum(1 for i in range(0x1F0200, 0x200000) if a[i] != b[i])
chk(n == 0, '세이브 구역 0x1F0200~ 무손상', '(바뀐 바이트 %d)' % n)

# ② 제목 기록 시작 주소 120개가 배포본과 같은가 (오늘 번 불변식)
def starts(d):
    p = 0x07A7E4; s = []
    for i in range(120):
        s.append(p)
        cnt = struct.unpack_from('<H', d, p)[0]; p += 2 + 4 + 2 * cnt
        rows = struct.unpack_from('<H', d, p)[0]; p += 2
        for r in range(rows):
            while d[p] != 0xFF: p += 1
            p += 1
    return s, p
sa, ea = starts(a); sb, eb = starts(b)
bad = [i + 1 for i in range(120) if sa[i] != sb[i]]
chk(not bad, '제목 기록 시작 주소 120개가 배포본과 동일',
    '(어긋난 첫 기록 %s → 처음 깨질 카드 %s)' % (bad[0] if bad else '-', (bad[0] + 1) if bad else '-'))
chk(eb == 0x07C642, '제목 기록 표가 0x07C642 에서 끝남', '(0x%06X)' % eb)

# ③ 순정이 쓰는 자리를 건드렸나 — 순정과 후보가 같아야 하는 곳은 아니지만,
#    순정에서 0xFF 가 아니었던 곳을 우리가 새로 덮었는지 본다(글자판 구역 한정)
lo, hi = 0x1E7C00, 0x1EBB20
n = sum(1 for i in range(lo, hi) if pr[i] != 0xFF)
chk(n == 0, '글자판 구역 0x1E7C00~0x1EBB20 은 순정에서 통째로 0xFF', '(순정 비-FF %d B)' % n)

# ④ 카드 목록 표가 가리키는 곳이 제목 글자판과 겹치나
T = 0x1EF5A0
ptrs = [struct.unpack_from('<I', b, T + 4 * i)[0] - 0x200000 for i in range(121)]
rec_ptr = struct.unpack_from('<I', b, 0x07A7E4 + 2)[0] - 0x200000
board_end = 0
p = 0x07A7E4
for i in range(120):
    cnt = struct.unpack_from('<H', b, p)[0]; p += 2
    ptr = struct.unpack_from('<I', b, p)[0] - 0x200000; p += 4
    offs = struct.unpack_from('<%dH' % cnt, b, p); p += 2 * cnt
    board_end = max(board_end, ptr + max(offs) + 16)
    rows = struct.unpack_from('<H', b, p)[0]; p += 2
    for r in range(rows):
        while b[p] != 0xFF: p += 1
        p += 1
clash = [i + 1 for i, x in enumerate(ptrs) if rec_ptr <= x < board_end]
chk(not clash, '카드 글자 목록이 제목 글자판(0x%06X~0x%06X)을 안 침범' % (rec_ptr, board_end), '(겹친 칸 %s)' % (clash[:5] or '없음'))

# ⑤ 타일 예산 — 카드마다 쓰는 색인이 cnt 안에 드나
p = 0x07A7E4; over = []
for i in range(120):
    cnt = struct.unpack_from('<H', b, p)[0]; p += 2 + 4 + 2 * cnt
    rows = struct.unpack_from('<H', b, p)[0]; p += 2
    mx = 0
    for r in range(rows):
        while b[p] != 0xFF: mx = max(mx, b[p]); p += 1
        p += 1
    if mx >= cnt: over.append((i + 1, mx, cnt))
chk(not over, '행 색인이 cnt 를 넘는 카드 없음', '(%s)' % (over[:3] or '없음'))

print('-' * 66)
print('관문 %s' % ('합격 — 화면 검사로 넘겨도 된다' if ok else '★불합격 — 굽기 전에 고쳐라'))
