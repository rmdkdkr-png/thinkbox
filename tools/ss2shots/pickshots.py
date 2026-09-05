# 촬영본 고르기 — 보스 대사(대사창 완성) · 엔딩 글(가장 많이 찍힌 장) · 최종 보스 화면
import pickle,os,sys,struct,zlib,io
NAMES={0:"겐쥬로",1:"시키",2:"아수라",3:"모로즈미",4:"하오마루",5:"갈포드",6:"나코루루",
       8:"리무루루",9:"한조",10:"쥬베이",11:"소게츠",12:"샬럿",13:"카즈키",14:"우쿄"}
OUT=os.path.expanduser("~/ss2/work_lang/v10/release_final/endings")
def stats(px):
    blk=wht=0; n=0
    for i in range(0,len(px),3*7):
        r,g,b=px[i],px[i+1],px[i+2]; n+=1
        if r<40 and g<40 and b<40: blk+=1
        elif r>200 and g>200 and b>200: wht+=1
    return blk*100//n, wht*100//n
def box(px):                       # 아래쪽 대사창: y 118~150 에 밝은 화소가 얼마나
    n=c=0
    for y in range(118,150):
        for x in range(0,160,2):
            i=(y*160+x)*3; n+=1
            if px[i]>200 and px[i+1]>200 and px[i+2]>200: c+=1
    return c*100//n
def ink(px):                       # 글 화소(밝은 것) 개수 — 많이 찍힌 장 고르기
    c=0
    for i in range(0,len(px),3*3):
        if px[i]>170 and px[i+1]>170: c+=1
    return c
def png(px,fn,s=1):
    out=bytearray()
    for y in range(152):
        line=bytearray()
        for x in range(160): line+=px[(y*160+x)*3:(y*160+x)*3+3]*s
        for _ in range(s): out+=b"\x00"+bytes(line)
    ck=lambda tg,d:(struct.pack(">I",len(d))+tg+d+struct.pack(">I",zlib.crc32(tg+d)&0xffffffff))
    open(fn,"wb").write(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",160*s,152*s,8,2,0,0,0))+ck(b"IDAT",zlib.compress(bytes(out),9))+ck(b"IEND",b""))
def pick(k,path):
    F=pickle.load(open(path,"rb")); S=[stats(px) for _,px in F]
    W=[i for i,(b,w) in enumerate(S) if w>60]
    end=W[0] if W else len(F)
    rows=[]
    # 보스 대사 — 대사창이 있는 장 중 글이 가장 많고 다음 장과 같은(완성) 것
    cand=[i for i in range(end) if box(F[i][1])>=3 and 55<S[i][0]<80 and 8<S[i][1]<20]
    if cand:
        best=max(cand,key=lambda i:ink(F[i][1]))
        png(F[best][1],"%s/%02d_%s_보스대사.png"%(OUT,k,NAMES[k]))
        rows.append((k,NAMES[k],"보스 대사","%02d_%s_보스대사.png"%(k,NAMES[k]),"표본%d"%best))
    # 엔딩 글 — 검정 페이지 중 글이 가장 많은 장
    ec=[i for i in range(end) if S[i][0]>85]
    if ec:
        best=max(ec,key=lambda i:ink(F[i][1]))
        png(F[best][1],"%s/%02d_%s_엔딩1.png"%(OUT,k,NAMES[k]))
        rows.append((k,NAMES[k],"엔딩 첫 화면","%02d_%s_엔딩1.png"%(k,NAMES[k]),"표본%d"%best))
    # 최종 보스 화면 — 대사 전 마지막 대전 장(검 30~60, 흰 <5)
    fc=[i for i in range((cand[0] if cand else end)) if 25<S[i][0]<60 and S[i][1]<5]
    if fc:
        png(F[fc[-1]][1],"%s/%02d_%s_최종보스직전.png"%(OUT,k,NAMES[k]))
        rows.append((k,NAMES[k],"최종 보스 직전","%02d_%s_최종보스직전.png"%(k,NAMES[k]),"표본%d"%fc[-1]))
    # 흰 화면 증거 1장
    if W:
        png(F[W[len(W)//2]][1],"%s/%02d_%s_흰화면.png"%(OUT,k,NAMES[k]))
        rows.append((k,NAMES[k],"흰 화면(고장)","%02d_%s_흰화면.png"%(k,NAMES[k]),"표본%d~%d"%(W[0],W[-1])))
    return rows
if __name__=="__main__":
    os.makedirs(OUT,exist_ok=True); allrows=[]
    for k in sorted(NAMES):
        for pre in ("n","h"):
            p=os.path.expanduser("~/ss2/tmp/end/%s%02d.pkl"%(pre,k))
            if os.path.exists(p):
                r=pick(k,p)
                if any(x[2]=="엔딩 첫 화면" for x in r) or pre=="h": allrows+=r; print(k,NAMES[k],[x[2] for x in r]); break
    with io.open("%s/endings.tsv"%OUT,"w",encoding="utf-8",newline="\n") as f:
        f.write("자리\t캐릭\t장면\t파일\t시점\n")
        for x in allrows: f.write("\t".join(str(v) for v in x)+"\n")
    print("총",len(allrows),"장")
