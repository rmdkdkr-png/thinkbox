# -*- coding: utf-8 -*-
"""표식 롬을 «안 본 화면»까지 끌고 다닌다 — 데모·컬렉션·설정·컨티뉴·엔딩.

훑은 화면만큼만 안다. 그래서 넣기 전에 넓히는 것이 싸다.
⚠ 엔딩 중에는 poke 를 멈춰야 한다(포크가 코어를 죽인다 — traps ⑪).
"""
import io, os, shutil, subprocess, sys, tempfile

RUN = "/mnt/c/Claude/KOF R2 한글/tools/ngprun"
CORE = "/home/dudu/m1/m31.so"
E = dict(os.environ); E["NGP_OPTS"] = "ngp_ss2sp=disabled"
ROM = os.path.expanduser("~/ss2/tmp/lb/probe.ngc")
OUT = os.path.expanduser("~/ss2/tmp/vrPROBE3"); os.makedirs(OUT, exist_ok=True)
V = lambda t: ["!vram %s" % t, "!" + t]
INV = ["!poke 1A46=128"]

# ① 데모/어트랙트 — 제목에서 손 떼고 오래 둔다(데모 싸움·순위·로고가 돈다)
A = []
for i in range(26): A += ["400 -"] + V("d%02d" % i)

# ② 메뉴 — 카드 콜렉션과 게임 설정
B = ["1960 -", "4 B", "120 -"]
B += ["4 D", "16 -"] * 3 + ["4 B", "200 -"] + V("col0") + ["200 -"] + V("col1") \
     + ["4 R", "30 -"] * 3 + V("col2") + ["4 A", "120 -"]
B += ["4 D", "16 -"] + ["4 B", "200 -"] + V("opt0") + ["4 D", "30 -"] + V("opt1") \
     + ["4 D", "30 -"] + V("opt2")

# ③ 컨티뉴 — 내가 져서 이어하기 화면을 띄운다
C = ["1960 -", "4 B", "120 -", "4 B", "120 -", "4 B", "120 -", "4 B", "2000 -"]
C += ["600 -", "!poke 1A46=0", "2 -", "!unpoke", "600 -", "!poke 1A46=0", "2 -", "!unpoke", "400 -"]
for i in range(10): C += ["60 -"] + V("cont%02d" % i)

# ④ 엔딩 — KO 블록 열 번 뒤 포크를 끊고 찍는다
KO = ["820 -", "!poke 1C46=0"] + INV + ["2 -", "!unpoke"] + INV \
     + ["700 -", "!poke 1C46=0"] + INV + ["2 -", "!unpoke"] + INV + ["900 -"]
D = ["1960 -", "4 B", "120 -", "4 B", "120 -", "4 B", "2000 -"] + INV
for _ in range(10): D += KO
D += ["820 -", "!poke 1C46=0"] + INV + ["2 -", "!unpoke"] + INV \
     + ["700 -", "!poke 1C46=0"] + INV + ["2 -", "!unpoke"]
for i in range(24): D += ["120 -"] + V("end%02d" % i)


def shoot(script, tag):
    t = tempfile.mkdtemp(); r = os.path.join(t, "r.ngc"); shutil.copy(ROM, r)
    io.open(os.path.join(t, "s.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(script) + "\n")
    subprocess.run([RUN, CORE, r, os.path.join(t, "s.txt"), os.path.join(t, "g")],
                   capture_output=True, text=True, env=E)
    n = 0
    for f in sorted(os.listdir(t)):
        if f.startswith("g"):
            shutil.copy(os.path.join(t, f), "%s/%s_%s" % (OUT, tag, f[1:].lstrip("_"))); n += 1
    print(tag, n, "파일")


if __name__ == "__main__":
    for name, sc in (("demo", A), ("menu", B), ("cont", C), ("end", D)):
        shoot(sc, name)
