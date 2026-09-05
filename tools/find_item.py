#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""그림 아이템 머리 찾기 — logo-items.md §3 을 그대로 자동화.

    find_item.py <rom> <prefix(.char/.scroll/.pal)> [plane 1|2] [r0 r1]

타이틀 VRAM 덤프의 평면 지도에서 (r0..r1) 행의 타일 색인열을 얻어, 롬에서 stride 2 로 «색인−k» 바이트열을 찾는다.
행 간격이 (칸수×2+2)로 이어지는 자리를 지도 시작으로 잡고, 뒤로 걸어 cnt16|ptr32|off16×cnt 를 복원한다.
출력: 아이템 주소, cnt, ptr, 행·칸 수, tile_base(k), pal_base, 뱅크 범위, 형제 아이템(같은 ptr). 프로파일 JSON 한 줄도 찍는다.
"""
import sys, re, collections, json
rom = open(sys.argv[1], "rb").read(); pre = sys.argv[2]
plane = int(sys.argv[3]) if len(sys.argv) > 3 else 1
r0 = int(sys.argv[4]) if len(sys.argv) > 4 else 0; r1 = int(sys.argv[5]) if len(sys.argv) > 5 else 15
sc = open(pre + ".scroll", "rb").read(); m = sc[(plane-1)*2048:plane*2048]
cells = {}
for i in range(0, 2048, 2):
    w = m[i] | (m[i+1] << 8); r = (i//2)//32; c = (i//2) % 32
    cells[(r, c)] = w
# 로고 후보 행: 비어 있지 않은 칸이 8개 이상인 행
rows = [r for r in range(r0, r1+1) if sum(1 for c in range(32) if cells[(r, c)] & 0x1ff) >= 8]
print("후보 행:", rows)
found = {}
for r in rows:
    cols = [c for c in range(32) if cells[(r, c)] & 0x1ff]
    c0, c1 = min(cols), max(cols)
    tiles = [cells[(r, c)] & 0x1ff for c in range(c0, c1+1)]
    for k in range(0, 512):
        pat = b"".join(re.escape(bytes([(t-k) & 0xff])) + b"." for t in tiles)
        mm = re.search(pat, rom, re.S)
        if mm:
            found[r] = (k, mm.start(), c0, c1); break
for r, (k, p, c0, c1) in sorted(found.items()):
    pals = [cells[(r, c)] >> 9 & 0x1f for c in range(c0, c1+1)]; pb = [rom[p+2*i+1] for i in range(c1-c0+1)]
    base = collections.Counter(pals[i] - (pb[i] & 0x3f)//2 for i in range(len(pals)) if not pb[i] & 0xC0)
    print("행 %2d: k=%d 지도@%06X 열 %d..%d pal_base 후보 %s" % (r, k, p, c0, c1, base.most_common(2)))
if not found: raise SystemExit("지도를 못 찾음 — 평면/행 범위를 바꿔 보라")
# 행 간격으로 지도 시작·칸 수 확정
rs = sorted(found); starts = [found[r][1] for r in rs]
gaps = collections.Counter(starts[i+1]-starts[i] for i in range(len(starts)-1))
stride = gaps.most_common(1)[0][0] if gaps else None
ncols = (stride - 2)//2 if stride else (found[rs[0]][3]-found[rs[0]][2]+1)
first = starts[0]
# 앞으로 더 있는 행(후보에서 빠진 빈 행)까지 되감기: 지도 시작 = 첫 행 시작에서 stride 씩 뒤로, ff ff 가 앞에 있으면 계속
mapstart = first
while stride and rom[mapstart-2:mapstart] == b"\xff\xff" and rom[mapstart-stride-2:mapstart-stride] != b"":
    cand = mapstart - stride
    # 그 앞 행도 (타일, 팔) 쌍처럼 보이면(팔레트바이트 짝수·작음) 계속
    if all(rom[cand+2*i+1] & 0x3f < 0x20 for i in range(ncols)): mapstart = cand
    else: break
hdr = mapstart - 1
item = None
for cnt in range(1, 512):
    a = hdr - 6 - 2*cnt
    if a < 0: break
    if (rom[a] | (rom[a+1] << 8)) == cnt and 0x200000 <= int.from_bytes(rom[a+2:a+6], "little") < 0x400000:
        item = (a, cnt, int.from_bytes(rom[a+2:a+6], "little")); break
if not item: raise SystemExit("cnt|ptr 머리를 못 찾음 (지도 시작 %06X, 헤더 %02X)" % (mapstart, rom[hdr]))
a, cnt, ptr = item
offs = [rom[a+6+2*i] | (rom[a+7+2*i] << 8) for i in range(cnt)]
# 행 수: stride 로 ff ff 이어지는 동안
pos = mapstart; nrows = 0
while rom[pos+stride-2:pos+stride] == b"\xff\xff" and nrows < 64: nrows += 1; pos += stride
k = found[rs[0]][0]
sib = [mm.start()-2 for mm in re.finditer(re.escape(ptr.to_bytes(3, "little")), rom) if 1 <= (rom[mm.start()-2] | (rom[mm.start()-1] << 8)) <= 400]
lo = ptr - 0x200000 + min(offs); hi = ptr - 0x200000 + max(offs) + 16
print("아이템 %06X cnt %d ptr %06X(파일) 헤더 %02X 지도 %06X..%06X %d행×%d칸 tile_base %d 타일 %06X..%06X 형제(같은 ptr) %s"
      % (a, cnt, ptr-0x200000, rom[hdr], mapstart, pos, nrows, ncols, k, lo, hi, ["%06X" % s for s in sib if s != a][:8]))
pb0 = collections.Counter()
for r in rs:
    k_, p, c0, c1 = found[r]
    for i in range(c1-c0+1):
        b = rom[p+2*i+1]
        if not b & 0xC0: pb0[(cells[(r, c0+i)] >> 9 & 0x1f) - (b & 0x3f)//2] += 1
pal_base = pb0.most_common(1)[0][0] if pb0 else 0
print(json.dumps({"item": "%06X" % a, "bank": "%06X" % lo, "bank_end": "%06X" % hi, "pal_dump": pre + ".pal", "pal_dump_off": "80" if plane == 1 else "100", "pal_base": pal_base & 0xF, "tile_base": k}, ensure_ascii=False))
