# -*- coding: utf-8 -*-
"""카드 120장 전수 검증 — 찍고, 재고, 사람이 볼 것만 골라 낸다.

    cardaudit.py <롬.ngc> [이름]          # 이름 기본값 = 롬 파일이름
    cardaudit.py --measure <찍은폴더> [이름]   # 이미 찍어 둔 것만 다시 잰다

내는 것 (~/ss2/tmp/cards/audit/<이름>/)
    shots/f###.png · d###.png     앞면·설명면 1배
    cards_audit.tsv               번호 · 제목 폭/좌우여백 · 제목 빈틈 · 설명 줄수 · 최장폭 · 빈틈 · 판정
    review.png                    ★ 표시된 카드만 모은 접촉 인화(사람이 볼 것)
    SUMMARY.md                    한 장 요약

판정 규칙 (수로 거르고, 애매한 것만 사람에게)
    ★제목없음      제목 잉크 0            → 반드시 본다
    ★설명없음      설명 줄 0
    ★명판넘침      제목 좌·우 여백 2 px 미만
    ★줄수초과      설명 13줄 이상(14줄이 한도, 15줄째가 No·별 줄 침범)
    ★뭉친칸        한 칸이 70% 넘게 차 있다 = 깨진 타일 의심(정상 한글은 25~45%)
    ★칸수차        글 표와 맞댄 잔차가 -8~+6 밖(줄 하나가 통째로 빠지면 여기 걸린다)
    설명글자칸     잉크가 있는 8 px 칸 수 — «빠진 글자»는 화면만으로 못 잡는다.
                   이 수를 1-f7 의 글자 수와 번호로 맞대는 것이 진짜 검사다
    △치우침        제목 좌우 여백 차 12 px 이상(가운데 정렬 확인용)
"""
import io, os, sys, subprocess, struct, zlib, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OUTROOT = os.path.expanduser("~/ss2/tmp/cards/audit")
ALLCARDS = os.path.expanduser("~/ss2/tmp/cards/ss2_allcards.ngc")
BASE = os.path.expanduser("~/ss2/work_lang/v10/release_final/ss2_v1.0_final.ngc")
TY0, TY1, TX0, TX1 = 9, 23, 38, 123          # 제목 명판 안쪽
BY0, BY1, BX0, BX1 = 24, 132, 36, 124        # 설명 글 상자 안쪽
PITCH = 8                                     # 줄 간격(실측)
LIMIT_LINES = 14                              # 15줄째가 No·별 줄을 침범한다
CENSUS = os.environ.get("CARDS_CENSUS",
    os.path.expanduser("~/ss2/work_lang/v10/review/census/cards_counts_for_audit.tsv"))
RESID_LO, RESID_HI = -8, 6                    # 멀쩡한 롬에서 잰 잔차 폭(-5~+3)에 여유를 준 값



def rd(fn):
    b = open(fn, "rb").read(); i = 8; idat = b""; W = H = 0
    while i < len(b):
        ln = struct.unpack(">I", b[i:i + 4])[0]; tp = b[i + 4:i + 8]; d = b[i + 8:i + 8 + ln]
        if tp == b"IHDR": W, H = struct.unpack(">II", d[:8])
        if tp == b"IDAT": idat += d
        i += 12 + ln
    raw = zlib.decompress(idat); st = W * 3; px = bytearray()
    for y in range(H): px += raw[y * (st + 1) + 1:(y + 1) * (st + 1)]
    return bytes(px)


def lum(px, y, x):
    i = (y * 160 + x) * 3
    return (px[i] * 3 + px[i + 1] * 6 + px[i + 2]) // 10


def gaps(cols, lo, hi, big):
    """cols = 잉크가 있는 x 목록. 글자 사이가 big px 이상 비면 «빈틈»으로 본다."""
    if not cols: return []
    out = []; prev = cols[0]
    for x in cols[1:]:
        if x - prev - 1 >= big: out.append((prev + 1, x - 1))
        prev = x
    return out


def title(px):
    xs = [x for x in range(TX0, TX1) if any(lum(px, y, x) > 150 for y in range(TY0, TY1))]
    if not xs: return dict(w=0, l=0, r=0, gaps=[])
    return dict(w=xs[-1] - xs[0] + 1, l=xs[0] - TX0, r=TX1 - 1 - xs[-1], gaps=gaps(xs, TX0, TX1, 12))


def body(px):
    """줄 수 · 최장 폭 · 글자 칸 수 · 뭉친 칸(깨진 타일 의심).

    글자는 8 px 칸에 놓인다. 칸마다 잉크를 세어 «찬 칸»을 글자로 보고,
    채움이 70% 를 넘으면 정상 한글이 아니다(깨진 타일).
    """
    rows = []
    for y in range(BY0, BY1):
        xs = [x for x in range(BX0, BX1) if lum(px, y, x) > 150]
        rows.append((y, xs))
    runs = []; cur = []
    for y, xs in rows:
        if xs: cur.append((y, xs))
        elif cur: runs.append(cur); cur = []
    if cur: runs.append(cur)
    lines = 0; wmax = 0; cells = 0; dense = []
    for r in runs:
        h = r[-1][0] - r[0][0] + 1
        k = max(1, round(h / PITCH)); lines += k
        for y, xs in r: wmax = max(wmax, xs[-1] - xs[0] + 1)
        for i in range(k):
            y0 = r[0][0] + i * PITCH; y1 = y0 + PITCH
            for cx in range(BX0 + 1, BX1 - 7, 8):
                ink = sum(1 for y in range(y0, min(y1, BY1)) for x in range(cx, cx + 8)
                          if lum(px, y, x) > 150)
                if ink == 0: continue
                cells += 1
                if ink > int(PITCH * 8 * 0.70): dense.append((y0, cx, ink))
    return dict(lines=lines, wmax=wmax, cells=cells, dense=dense)


def png(px, fn, s=1):
    out = bytearray()
    for y in range(152):
        line = bytearray()
        for x in range(160): line += px[(y * 160 + x) * 3:(y * 160 + x) * 3 + 3] * s
        for _ in range(s): out += b"\x00" + bytes(line)
    ck = lambda tg, d: (struct.pack(">I", len(d)) + tg + d + struct.pack(">I", zlib.crc32(tg + d) & 0xffffffff))
    open(fn, "wb").write(b"\x89PNG\r\n\x1a\n" + ck(b"IHDR", struct.pack(">IIBBBBB", 160 * s, 152 * s, 8, 2, 0, 0, 0))
                         + ck(b"IDAT", zlib.compress(bytes(out), 9)) + ck(b"IEND", b""))


def sheet(imgs, fn, cols=6):
    rows = (len(imgs) + cols - 1) // cols; o = bytearray()
    for rr in range(rows):
        for y in range(152):
            line = bytearray()
            for c in range(cols):
                i = rr * cols + c
                line += imgs[i][y * 480:(y + 1) * 480] if i < len(imgs) else bytes(480)
            o += b"\x00" + bytes(line)
    ck = lambda tg, d: (struct.pack(">I", len(d)) + tg + d + struct.pack(">I", zlib.crc32(tg + d) & 0xffffffff))
    open(fn, "wb").write(b"\x89PNG\r\n\x1a\n" + ck(b"IHDR", struct.pack(">IIBBBBB", 160 * cols, 152 * rows, 8, 2, 0, 0, 0))
                         + ck(b"IDAT", zlib.compress(bytes(o), 9)) + ck(b"IEND", b""))


def make_allcards(rom):
    """올카드 세이브 블록 72 B 를 얹은 사본을 만든다(컬렉션에서 120장을 다 봐야 한다)."""
    base = open(BASE, "rb").read(); allc = open(ALLCARDS, "rb").read()
    p = bytearray(open(rom, "rb").read())
    for i in range(len(base)):
        if base[i] != allc[i]: p[i] = allc[i]
    out = os.path.join(OUTROOT, "_allcards.ngc")
    open(out, "wb").write(bytes(p)); return out


def shoot(rom, shots):
    """줄마다(8장) 찬 부팅 — 누름 하나가 새도 그 줄만 어긋난다."""
    os.makedirs(shots, exist_ok=True)
    e = dict(os.environ); e["SS2ROM"] = make_allcards(rom)
    for r in range(15):
        a, b = r * 8 + 1, r * 8 + 8
        subprocess.run([sys.executable, os.path.join(HERE, "cardshot.py"), str(a), str(b), shots],
                       env=e, capture_output=True, text=True)
        print("  줄 %2d (%3d~%3d) 찍음" % (r, a, b), flush=True)


def load_census():
    """글 담당 표(번호·총코드·글자·공백·줄바꿈·아이콘·줄수)를 읽는다. 없으면 빈 채로 간다."""
    if not os.path.exists(CENSUS): return {}
    c = {}
    for l in io.open(CENSUS, encoding="utf-8").read().splitlines()[1:]:
        p = l.split("\t")
        if len(p) < 7: continue
        c[int(p[0])] = dict(ch=int(p[2]), sp=int(p[3]), nl=int(p[4]), ic=int(p[5]))
    return c


def audit(shots, name):
    out = os.path.join(OUTROOT, name); os.makedirs(out, exist_ok=True)
    cen = load_census()
    rows = []; flagged = []
    for n in range(1, 121):
        f = "%s/d%03d.png" % (shots, n)
        if not os.path.exists(f):
            rows.append((n, 0, 0, 0, 0, 0, 0, 0, "", "", 0, "★없음(못 찍음)")); flagged.append(n); continue
        px = rd(f); t = title(px); b = body(px)
        tags = []
        if t["w"] == 0: tags.append("★제목없음")
        if b["lines"] == 0: tags.append("★설명없음")
        if t["w"] and (t["l"] < 2 or t["r"] < 2): tags.append("★명판넘침")
        if b["lines"] > LIMIT_LINES - 1: tags.append("★줄수초과")
        if b["dense"]: tags.append("★뭉친칸%d" % len(b["dense"]))
        exp = resid = ""
        if n in cen:
            # 화면 칸 수 ≈ 글자 + 아이콘 + 줄수 (멀쩡한 롬에서 잰 관계, 잔차 -5~+3)
            exp = cen[n]["ch"] + cen[n]["ic"] + b["lines"]
            resid = b["cells"] - exp
            if resid < RESID_LO or resid > RESID_HI: tags.append("★칸수차%+d" % resid)

        if t["w"] and abs(t["l"] - t["r"]) >= 12: tags.append("△치우침%+d" % (t["r"] - t["l"]))
        v = "·" if not tags else " ".join(tags)
        rows.append((n, t["w"], t["l"], t["r"], abs(t["l"] - t["r"]), b["lines"], b["wmax"], b["cells"], exp, resid, len(b["dense"]), v))
        if any(x.startswith("★") for x in tags): flagged.append(n)
    with io.open("%s/cards_audit.tsv" % out, "w", encoding="utf-8", newline="\n") as f:
        f.write("번호\t제목폭px\t제목좌여백\t제목우여백\t좌우차\t설명줄수\t설명최장폭px\t설명글자칸\t기대칸\t차이\t뭉친칸\t판정\n")
        for r in rows: f.write("\t".join(str(x) for x in r) + "\n")
    if flagged:
        sheet([rd("%s/d%03d.png" % (shots, n)) for n in flagged if os.path.exists("%s/d%03d.png" % (shots, n))],
              "%s/review.png" % out)
    bad = [r for r in rows if r[11] != "·"]
    ln = {}
    for r in rows: ln[r[5]] = ln.get(r[5], 0) + 1
    L = ["# 카드 전수 검증 — %s" % name, "",
         "찍은 것 %d장 · 표 `cards_audit.tsv` · 사람이 볼 카드 %d장 `review.png`" % (len(rows), len(flagged)), "",
         "| 항목 | 값 |", "|---|---|",
         "| 제목 폭 최대 | %d px (명판 안쪽 85 px) |" % max(r[1] for r in rows),
         "| 제목 여백 최소 | 좌 %d px · 우 %d px |" % (min(r[2] for r in rows), min(r[3] for r in rows)),
         "| 설명 줄 수 | " + " · ".join("%d줄 %d장" % (k, v) for k, v in sorted(ln.items())) + " |",
         "| 설명 최장 폭 | %d px |" % max(r[6] for r in rows),
         "| 설명 글자 칸 합계 | %d칸 |" % sum(r[7] for r in rows),
         ("| 글 표와 맞댄 잔차 | %s |" % (" · ".join("%+d: %d장" % (k, v) for k, v in sorted(
             __import__("collections").Counter(r[9] for r in rows if r[9] != "").items()))
             or "글 표 없음")),
         "| 제목 좌우 여백 차 최대 | %d px |" % max(r[4] for r in rows),
         "| ★ 걸린 카드 | %d장 |" % len([r for r in rows if "★" in r[11]]),
         "| △ 확인 권고 | %d장 |" % len([r for r in rows if "△" in r[11] and "★" not in r[11]]), ""]
    if bad:
        L += ["## 걸린 카드", "", "| 번호 | 판정 |", "|---|---|"] + ["| %d | %s |" % (r[0], r[11]) for r in bad]
    else:
        L += ["**걸린 카드 없음.**"]
    io.open("%s/SUMMARY.md" % out, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("★%d장 · △%d장 · 표와 요약: %s" % (len([r for r in rows if "★" in r[11]]),
                                            len([r for r in rows if "△" in r[11] and "★" not in r[11]]), out))
    return rows


if __name__ == "__main__":
    os.makedirs(OUTROOT, exist_ok=True)
    if sys.argv[1] == "--measure":
        shots = os.path.expanduser(sys.argv[2])
        audit(shots, sys.argv[3] if len(sys.argv) > 3 else os.path.basename(shots.rstrip("/")))
    else:
        rom = os.path.expanduser(sys.argv[1])
        name = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(rom).rsplit(".", 1)[0]
        shots = os.path.join(OUTROOT, name, "shots")
        print("찍는다 —", rom, flush=True); shoot(rom, shots)
        audit(shots, name)
