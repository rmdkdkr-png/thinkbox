# -*- coding: utf-8 -*-
"""카드 획득 팝업 — 대전 한 판을 이기고 그 뒤 화면을 촘촘히 찍는다."""
import io,os,subprocess,sys,tempfile,shutil,pickle
RUN="/mnt/c/Claude/KOF R2 한글/tools/ngprun"; CORE="/home/dudu/m1/m31.so"
E=dict(os.environ); E["NGP_OPTS"]="ngp_ss2sp=disabled"
ROM=os.path.expanduser(os.environ.get("SS2ROM","~/ss2/work_lang/v10/release_final/varC_quote_glyph.ngc"))
k=int(sys.argv[1]) if len(sys.argv)>1 else 2
NS=int(sys.argv[2]) if len(sys.argv)>2 else 70
tag=sys.argv[3] if len(sys.argv)>3 else "pop"
r,c=divmod(k,5)
INV=["!poke 1A46=128"]
script=["1960 -","8 B","120 -","8 B","120 -"]+["8 D","20 -"]*r+((["8 L","20 -"]*(2-c)) if c<2 else (["8 R","20 -"]*(c-2)))+["8 B","120 -","8 B","2000 -"]+INV
script+=["600 -","!poke 1C46=0"]+INV+["2 -","!unpoke"]+INV+["700 -","!poke 1C46=0"]+INV+["2 -","!unpoke"]
tags=[]
for i in range(NS): tg="p%03d"%i; tags.append(tg); script+=["24 -","!"+tg]
t=tempfile.mkdtemp(); rom=os.path.join(t,"r.ngc"); shutil.copy(ROM,rom)
io.open(os.path.join(t,"s.txt"),"w",encoding="utf-8",newline="\n").write("\n".join(script)+"\n")
subprocess.run([RUN,CORE,rom,os.path.join(t,"s.txt"),os.path.join(t,"g")],capture_output=True,text=True,env=E)
def ppm(p):
    b=open(p,"rb").read(); j=0; tk=[]
    while len(tk)<4:
        while b[j:j+1].isspace(): j+=1
        kk=j
        while not b[kk:kk+1].isspace(): kk+=1
        tk.append(b[j:kk]); j=kk
    return b[j+1:]
F=[(i,ppm(os.path.join(t,"g_%s.ppm"%tg))) for i,tg in enumerate(tags) if os.path.exists(os.path.join(t,"g_%s.ppm"%tg))]
pickle.dump(F,open(os.path.expanduser("~/ss2/tmp/cards/%s%02d.pkl"%(tag,k)),"wb"))
print("%s 자리%d 장 %d"%(tag,k,len(F)))
