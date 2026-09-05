# -*- coding: utf-8 -*-
"""부팅부터 제목 화면까지 훑어 찍는다 — v12·v13 을 같은 대본으로.

로고가 바뀐 판이라 **같은 순간을 견줘야** 한다. 프레임 번호로 짝지으면 안 되고
(traps ⑬) 같은 대본에서 같은 태그로 뜬 것끼리 본다.
"""
import io, os, shutil, subprocess, tempfile

RUN = "/mnt/c/Claude/KOF R2 한글/tools/ngprun"
CORE = "/home/dudu/m1/m31.so"
E = dict(os.environ); E["NGP_OPTS"] = "ngp_ss2sp=disabled"
OUT = os.path.expanduser("~/ss2/tmp/title2"); os.makedirs(OUT, exist_ok=True)

STEP, N = 300, 24
SCRIPT = []
for i in range(N):
    SCRIPT += ["%d -" % STEP, "!b%02d" % i]


def shoot(rom, tag):
    t = tempfile.mkdtemp(); r = os.path.join(t, "r.ngc"); shutil.copy(os.path.expanduser(rom), r)
    io.open(os.path.join(t, "s.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(SCRIPT) + "\n")
    subprocess.run([RUN, CORE, r, os.path.join(t, "s.txt"), os.path.join(t, "g")],
                   capture_output=True, text=True, env=E)
    n = 0
    for f in sorted(os.listdir(t)):
        if f.startswith("g"):
            shutil.copy(os.path.join(t, f), "%s/%s_%s" % (OUT, tag, f[1:].lstrip("_"))); n += 1
    print(tag, n, "파일")


if __name__ == "__main__":
    shoot("~/ss2/work_lang/v10/release_final/cards_v12_final.ngc", "v12")
    shoot("~/ss2/work_lang/v10/release_final/cards_v13_final.ngc", "v13")
