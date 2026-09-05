# 엔딩·보스 촬영 — KO 블록 N개 뒤 «포크를 멈추고» 촘촘히 찍는다(엔딩 중 포크가 코어를 죽인다)
import io,os,subprocess,sys,tempfile,shutil,pickle
RUN="/mnt/c/Claude/KOF R2 한글/tools/ngprun"; CORE="/home/dudu/m1/m31.so"
E=dict(os.environ); E["NGP_OPTS"]="ngp_ss2sp=disabled"
ROM=os.path.expanduser(os.environ.get("SS2ROM","~/ss2/work_lang/v10/release_final/ss2_v1.0_final.ngc"))
k=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 10
NS=int(sys.argv[3]) if len(sys.argv)>3 else 320
STEP=12
r,c=divmod(k,5)
INV=["!poke 1A46=128"]
KO=["820 -","!poke 1C46=0"]+INV+["2 -","!unpoke"]+INV+["700 -","!poke 1C46=0"]+INV+["2 -","!unpoke"]+INV+["900 -"]
script=["1960 -","4 B","120 -","4 B","120 -"]+["4 D","12 -"]*r+((["4 L","12 -"]*(2-c)) if c<2 else (["4 R","12 -"]*(c-2)))+["4 B","120 -","4 B","2000 -"]+INV
for _ in range(N): script+=KO
script+=["820 -","!poke 1C46=0"]+INV+["2 -","!unpoke"]+INV+["700 -","!poke 1C46=0"]+INV+["2 -","!unpoke"]
tags=[]
for i in range(NS): tg="e%03d"%i; tags.append(tg); script+=["%d -"%STEP,"!"+tg]
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
out=os.path.expanduser("~/ss2/tmp/end/k%02d.pkl"%k); os.makedirs(os.path.dirname(out),exist_ok=True)
pickle.dump(F,open(out,"wb")); print("자리%d 장 %d"%(k,len(F)))
