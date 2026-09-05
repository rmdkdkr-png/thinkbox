# 대사창 모으기 — 처음부터 9블록까지 훑어 «초상 + 대사창»이 있는 장을 전부 모은다
import io,os,subprocess,sys,tempfile,shutil,pickle
RUN="/mnt/c/Claude/KOF R2 한글/tools/ngprun"; CORE="/home/dudu/m1/m31.so"
E=dict(os.environ); E["NGP_OPTS"]="ngp_ss2sp=disabled"
ROM=os.path.expanduser("~/ss2/work_lang/v10/release_final/varC_quote_glyph.ngc")
k=int(sys.argv[1]); r,c=divmod(k,5)
INV=["!poke 1A46=128"]
script=["1960 -","4 B","120 -","4 B","120 -"]+["4 D","12 -"]*r+((["4 L","12 -"]*(2-c)) if c<2 else (["4 R","12 -"]*(c-2)))+["4 B","120 -","4 B","2000 -"]+INV
tags=[]; n=0
def wait(f,step=24):
    global n; out=[]
    for _ in range(f//step):
        tg="d%04d"%n; tags.append(tg); n+=1; out+=["%d -"%step,"!"+tg]
    return out
for st in range(9):
    script+=wait(820)+["!poke 1C46=0"]+INV+["2 -","!unpoke"]+INV+wait(700)+["!poke 1C46=0"]+INV+["2 -","!unpoke"]+INV+wait(900)
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
pickle.dump(F,open(os.path.expanduser("~/ss2/tmp/end/dlg%02d.pkl"%k),"wb"))
print("자리%d 대사 훑기 %d장"%(k,len(F)))
