# 자산 만들기 — VRAM 덤프(평면0) 사각 구역 → JSON(칸·타일·팔레트·반전 + 타일별 롬 주소) · 미리보기 · 마스크
import sys,os,json,struct,zlib
sys.path.insert(0,"."); from vrdec import *
ROM={"p":os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc"),
     "h":os.path.expanduser("~/ss2/work_lang/v10/release_final/ss2_v1.0_final.ngc")}
def build(lab,tag,rows,cols,key,outdir):
    d=load(tag); rom=open(ROM[lab],"rb").read()
    cells=[]; tiles={}
    use={}                                     # 타일 색인 → 화면 전체에서 쓰는 칸 수
    for r in range(32):
        for c in range(32):
            t,hf,vf,p=cell(d["scroll"],0,r,c); use[t]=use.get(t,0)+1
    pals={}
    for r in rows:
        for c in cols:
            t,hf,vf,p=cell(d["scroll"],0,r,c)
            cells.append([r,c,t,p,hf,vf]); pals.setdefault(p,[pal(d["pal"],p,i) for i in range(4)])
            if t not in tiles:
                data=d["char"][t*16:t*16+16]
                if not any(data): tiles[t]="blank"
                else:
                    hits=[]; i=rom.find(data)
                    while i>=0 and len(hits)<3: hits.append(i); i=rom.find(data,i+1)
                    tiles[t]=("%06X"%hits[0]) if len(hits)==1 else (("%06X"%hits[0]+"?") if hits else "없음")
    js=dict(name=key,rom=lab,plane=1,rows=list(rows),cols=list(cols),
            tiles={str(k):v for k,v in tiles.items()},
            palettes={str(k):[list(x) for x in v] for k,v in pals.items()},
            budget=dict(cells=len(cells),unique_tiles=len([v for v in tiles.values() if v!="blank"])),
            cells=cells)
    os.makedirs(outdir,exist_ok=True)
    json.dump(js,open("%s/%s_%s.json"%(outdir,lab,key),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    # 미리보기 4배
    W=len(cols)*8; H=len(rows)*8; img=bytearray(W*H*3)
    for r,c,t,p,hf,vf in cells:
        px=tilepix(d["char"],t)
        for y in range(8):
            for x in range(8):
                v=px[7-y if vf else y][7-x if hf else x]
                col=(255,0,255) if v==0 else pal(d["pal"],p,v)
                o=(((rows.index(r)*8+y)*W)+(cols.index(c)*8+x))*3; img[o:o+3]=bytes(col)
    png(img,W,H,4,"%s/%s_%s.png"%(outdir,lab,key))
    # 마스크(칸당 16px): 흰=이 칸만의 타일 · 주황=공유 · 검정=빈 타일
    mW=len(cols)*16; mH=len(rows)*16; m=bytearray(mW*mH*3)
    free=0
    for r,c,t,p,hf,vf in cells:
        if tiles[t]=="blank": col=(0,0,0)
        elif use[t]>1: col=(255,140,0)
        else: col=(255,255,255); free+=1
        for y in range(16):
            for x in range(16):
                o=(((rows.index(r)*16+y)*mW)+(cols.index(c)*16+x))*3; m[o:o+3]=bytes(col)
    png(m,mW,mH,1,"%s/p_%s_mask.png"%(outdir,key) if lab=="p" else "%s/%s_%s_mask.png"%(outdir,lab,key))
    print("%s %s  칸%d 고유타일%d 자유칸%d"%(lab,key,len(cells),js["budget"]["unique_tiles"],free))
    return js
def png(img,W,H,S,fn):
    out=bytearray()
    for y in range(H):
        line=bytearray()
        for x in range(W): line+=img[(y*W+x)*3:(y*W+x)*3+3]*S
        for _ in range(S): out+=b"\x00"+bytes(line)
    ck=lambda tg,dd:(struct.pack(">I",len(dd))+tg+dd+struct.pack(">I",zlib.crc32(tg+dd)&0xffffffff))
    open(fn,"wb").write(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",W*S,H*S,8,2,0,0,0))+ck(b"IDAT",zlib.compress(bytes(out),9))+ck(b"IEND",b""))
if __name__=="__main__":
    R=list(range(5,10)); C=[10,11,12]
    o=os.path.expanduser("~/ss2/tmp/asset")
    build("p","p_iza2",R,C,"izatop",o); build("h","h_iza2",R,C,"izatop",o)
