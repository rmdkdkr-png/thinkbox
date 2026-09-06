# -*- coding: utf-8 -*-
"""회전 배너 삽입판 촬영 — 1·2·3회전을 한 롬에서 다 뜬다.

⚠ 롬이 다르면 같은 대본도 다른 순간에 닿는다(traps ⑬). 그래서 태그를 믿지 말고
   **화면에 무엇이 떠 있는지로** 골라야 한다 — 고르는 것은 roundpick.py 가 한다.
"""
import io, os, shutil, subprocess, sys, tempfile

RUN = "/mnt/c/Claude/KOF R2 한글/tools/ngprun"
CORE = "/home/dudu/m1/m31.so"
E = dict(os.environ); E["NGP_OPTS"] = "ngp_ss2sp=disabled"
ROM = os.path.expanduser(os.environ.get("RC_ROM","~/ss2/work_lang/v10/release_final/test_rounds.ngc"))
OUT = os.path.expanduser(os.environ.get("RC_OUT","~/ss2/tmp/vrTR")); os.makedirs(OUT, exist_ok=True)
INV = ["!poke 1A46=128"]
V = lambda t: ["!vram %s" % t, "!" + t]

# ① 1회전 — 싸움 초반(자아·당당히 뒤에 회전 배너가 뜬다)
S_IZA = ["1960 -", "4 B", "120 -", "4 B", "120 -", "4 B", "120 -", "4 B", "2000 -", "460 -"] \
        + V("iza1") + ["60 -"] + V("iza2") + ["60 -"] + V("iza3")
# ② 2회전 — 1라운드를 이기고 KO 뒤 창을 훑는다
S_R2 = ["1960 -", "4 B", "120 -", "4 B", "120 -", "4 B", "120 -", "4 B", "2000 -"] + INV \
       + ["600 -", "!poke 1C46=0"] + INV + ["2 -", "!unpoke"] + INV
for i in range(22): S_R2 += ["40 -"] + V("r2_%02d" % i)
# ③ 3회전 — 1라운드 지고 2라운드 이겨 1-1 을 만든다
S_R3 = ["1960 -", "4 B", "120 -", "4 B", "120 -", "4 B", "120 -", "4 B", "2000 -"] \
       + ["600 -", "!poke 1A46=0", "2 -", "!unpoke", "900 -"] \
       + ["600 -", "!poke 1C46=0", "2 -", "!unpoke"]
for i in range(26): S_R3 += ["40 -"] + V("t%02d" % i)


def shoot(script, rom=ROM):
    t = tempfile.mkdtemp(); r = os.path.join(t, "r.ngc"); shutil.copy(rom, r)
    io.open(os.path.join(t, "s.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(script) + "\n")
    subprocess.run([RUN, CORE, r, os.path.join(t, "s.txt"), os.path.join(t, "g")],
                   capture_output=True, text=True, env=E)
    n = 0
    for f in sorted(os.listdir(t)):
        if f.startswith("g"):
            shutil.copy(os.path.join(t, f), "%s/%s" % (OUT, f[1:].lstrip("_"))); n += 1
    return n


if __name__ == "__main__":
    for name, sc in (("1회전 계열", S_IZA), ("2회전 계열", S_R2), ("3회전 계열", S_R3)):
        print(name, shoot(sc), "파일")
