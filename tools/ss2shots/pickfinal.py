# -*- coding: utf-8 -*-
"""고친 롬(varC)으로 찍은 것에서 촬영본을 고른다 — 엔딩 쪽 1·2, 보스 대사, 최종 보스 직전."""
import pickle,os,sys,struct,zlib,io
sys.path.insert(0,"."); from endpick import isend
NAMES={0:"겐쥬로",1:"시키",2:"아수라",3:"모로즈미",4:"하오마루",5:"갈포드",6:"나코루루",
       8:"리무루루",9:"한조",10:"쥬베이",11:"소게츠",12:"샬럿",13:"카즈키",14:"우쿄"}
OUT=os.path.expanduser("~/ss2/work_lang/v10/release_final/endings")
def stats(px):
    blk=wht=n=0
    for i in range(0,len(px),3*7):
        r,g,b=px[i],px[i+1],px[i+2]; n+=1
        if r<40 and g<40 and b<40: blk+=1
        elif r>200 and g>200 and b>200: wht+=1
    return blk*100//n, wht*100//n
def band(px,y0,y1):
    c=0
    for y in range(y0,y1):
        for x in range(8,152):
            i=(y*160+x)*3
            if px[i]>170 and px[i+1]>170 and px[i+2]>170: c+=1
    return c
def inktop(px): return band(px,4,72)      # 엔딩 글은 화면 위쪽에 쌓인다
def inkbot(px): return band(px,80,146)    # 스태프롤은 아래쪽에도 글이 있다
def box(px):
    n=c=0
    for y in range(118,150):
        for x in range(0,160,2):
            i=(y*160+x)*3; n+=1
            if px[i]>200 and px[i+1]>200 and px[i+2]>200: c+=1
    return c*100//n
def png(px,fn,s=1):
    out=bytearray()
    for y in range(152):
        line=bytearray()
        for x in range(160): line+=px[(y*160+x)*3:(y*160+x)*3+3]*s
        for _ in range(s): out+=b"\x00"+bytes(line)
    ck=lambda tg,d:(struct.pack(">I",len(d))+tg+d+struct.pack(">I",zlib.crc32(tg+d)&0xffffffff))
    open(fn,"wb").write(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",160*s,152*s,8,2,0,0,0))+ck(b"IDAT",zlib.compress(bytes(out),9))+ck(b"IEND",b""))
def pages(F,W):
    """엔딩 창에서 «글이 쌓였다가 지워지는» 덩어리를 나눈다 → 덩어리마다 가장 많이 쌓인 장"""
    v=[(i,inktop(F[i][1])) for i in W]
    mx=max(x[1] for x in v) if v else 0
    if not mx: return []
    floor=max(8,mx//12); runs=[]; cur=[]
    for i,c in v:
        if c>floor: cur.append((i,c))
        elif cur: runs.append(cur); cur=[]
    if cur: runs.append(cur)
    return [max(r,key=lambda x:x[1])[0] for r in runs if max(x[1] for x in r)>mx//4]
def pick(k):
    p=os.path.expanduser("~/ss2/tmp/end/g%02d.pkl"%k)
    if not os.path.exists(p): p=os.path.expanduser("~/ss2/tmp/end/f%02d.pkl"%k)
    if not os.path.exists(p): return []
    F=pickle.load(open(p,"rb")); S=[stats(px) for _,px in F]
    W=[i for i,(_,px) in enumerate(F) if isend(px)]
    rows=[]
    # 엔딩 글은 스태프롤보다 먼저 시작한다 — 창의 앞머리만 본다(뒤는 스태프롤 글씨가 섞인다)
    W2=[i for i in W if i<=W[0]+88] if W else []
    pg=pages(F,W2 or W)
    # 이 게임의 엔딩은 «한 쪽»이다 — 글이 그 판에 다 쌓이고 곧바로 스태프롤로 넘어간다
    for i in pg[:1]:
        fn="%02d_%s_엔딩.png"%(k,NAMES[k]); png(F[i][1],"%s/%s"%(OUT,fn))
        rows.append((k,NAMES[k],"엔딩 화면(글 완성)",fn,"표본%d"%i))
    first=W[0] if W else len(F)
    cand=[i for i in range(first) if box(F[i][1])>=3 and 55<S[i][0]<80 and 8<S[i][1]<20]
    if cand:
        b=max(cand,key=lambda i:inktop(F[i][1])+box(F[i][1])*50)
        fn="%02d_%s_보스대사.png"%(k,NAMES[k]); png(F[b][1],"%s/%s"%(OUT,fn))
        rows.append((k,NAMES[k],"보스 대사",fn,"표본%d"%b))
    fc=[i for i in range(first) if 25<S[i][0]<60 and S[i][1]<5]
    if fc:
        fn="%02d_%s_최종보스직전.png"%(k,NAMES[k]); png(F[fc[-1]][1],"%s/%s"%(OUT,fn))
        rows.append((k,NAMES[k],"최종 보스 직전",fn,"표본%d"%fc[-1]))
    return rows
if __name__=="__main__":
    import glob
    for f in glob.glob(OUT+"/*.png"):
        if "_엔딩버그_" not in f: os.remove(f)
    allrows=[]
    for k in sorted(NAMES):
        r=pick(k); allrows+=r; print(k,NAMES[k],[x[2] for x in r],flush=True)
    with io.open("%s/endings.tsv"%OUT,"w",encoding="utf-8",newline="\n") as f:
        f.write("자리\t캐릭\t장면\t파일\t시점\n")
        for x in allrows: f.write("\t".join(str(v) for v in x)+"\n")
    print("총",len(allrows),"장")
