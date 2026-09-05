# -*- coding: utf-8 -*-
"""배포 후보 관문 — 본부 몫. 이식소 화면 검사와 별개로 롬만 보고 거는 것."""
import io, os, sys, struct, hashlib

R = os.path.expanduser('~/ss2/work_lang/v10/release_final/')
BASE = R + 'ss2_v1.0_final.ngc'
CAND = os.path.expanduser(sys.argv[1]) if len(sys.argv) > 1 else R + 'cards_v9_final.ngc'
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

# ① 세이브 구역 — 기본판은 0 B, 올카드판은 «정해진 72 B 만» 이어야 한다
SAVE_OK = ((0x1F0300, 0x1F0358), (0x1F03E6, 0x1F0400))   # 올카드가 바꾸는 자리(카드 소유 표시)
diff = [i for i in range(0x1F0200, 0x200000) if a[i] != b[i]]
if 'allcards' in os.path.basename(CAND):
    outside = [i for i in diff if not any(lo <= i < hi for lo, hi in SAVE_OK)]
    chk(not outside and len(diff) == 72,
        '올카드판 — 세이브 구역이 정해진 72 B 만 다름',
        '(바뀐 %d B · 범위 밖 %d B)' % (len(diff), len(outside)))
else:
    chk(not diff, '세이브 구역 0x1F0200~ 무손상', '(바뀐 바이트 %d)' % len(diff))

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

# ②-보탬 ★진짜 불변식: 색인표 0x0822D2(u16×120)가 각 기록의 시작을 가리켜야 한다.
#   게임이 읽는 것은 «순서대로 걷기»가 아니라 이 표다. 어긋나면 그 카드부터 화면이 무너진다
#   (실측: 어긋난 첫 기록 번호 == 처음 깨지는 카드 번호, 롬 11개 전부 일치).
tbl = [0x0722D2 + struct.unpack_from('<H', b, 0x0822D2 + 2 * i)[0] for i in range(120)]
off = [i + 1 for i in range(120) if tbl[i] != sb[i]]
chk(not off, '색인표 0x0822D2 가 기록 시작 120개와 맞음',
    '(어긋난 첫 카드 %s → 그 카드부터 깨진다)' % (off[0] if off else '-'))

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

# ⑥ ★설명 글월이 «제자리에 같은 길이로» 있나
#    글을 옮기거나 길이를 바꾸면 목록과 어긋나, 화면에 «깨진 글자»가 아니라 «멀쩡한 다른 글자»가
#    뜬다 — 칸 수·줄 수·폭 어느 판정기에도 안 걸린다(2026-09-06 실측: 옮긴 넷만 깨졌다).
#    앞서 쓰던 「안 쓰는 슬롯」 항은 헛경보였다 — 멀쩡한 카드에도 남는 슬롯이 생긴다.
STRT = 0x0319EB
def desc(d):
    out = []
    for i in range(120):
        off = struct.unpack_from('<H', d, STRT + 2 * i)[0]
        a0 = STRT + off; e0 = a0
        while d[e0] != 0xFF: e0 += 1
        out.append((a0, e0 - a0))
    return out
da, db = desc(a), desc(b)
moved = [(i + 1, da[i], db[i]) for i in range(120) if da[i] != db[i]]
chk(not moved, '설명 글월이 배포본과 같은 자리·같은 길이',
    '(옮겨진 카드 %s)' % ([('%d 0x%06X→0x%06X %d→%d' % (n, x[0], y[0], x[1], y[1])) for n, x, y in moved[:6]] or '없음'))

print('-' * 66)
print('관문 %s' % ('합격 — 화면 검사로 넘겨도 된다' if ok else '★불합격 — 굽기 전에 고쳐라'))
