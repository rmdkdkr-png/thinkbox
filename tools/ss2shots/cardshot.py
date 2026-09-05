# -*- coding: utf-8 -*-
"""카드 촬영 — 번호를 주면 그 카드의 앞면과 설명면을 찍는다.

    cardshot.py <시작> <끝> [출력폴더]        번호는 1~120

목록은 한 줄 8칸 · 15줄. 커서는 1번에서 시작하니 (n-1)//8 만큼 아래로, (n-1)%8 만큼 오른쪽으로.
올카드 롬으로 돌린다(종류 120/120). 롬은 새 폴더에 복사해 쓴다 — 롬 옆 .flash 가 롬 세이브를 이긴다.
"""
import io,os,subprocess,sys,tempfile,shutil,struct,zlib
RUN="/mnt/c/Claude/KOF R2 한글/tools/ngprun"; CORE="/home/dudu/m1/m31.so"
E=dict(os.environ); E["NGP_OPTS"]="ngp_ss2sp=disabled"
ROM=os.path.expanduser(os.environ.get("SS2ROM","~/ss2/tmp/cards/ss2_allcards.ngc"))
def png(px,fn,s=1):
    out=bytearray()
    for y in range(152):
        line=bytearray()
        for x in range(160): line+=px[(y*160+x)*3:(y*160+x)*3+3]*s
        for _ in range(s): out+=b"\x00"+bytes(line)
    ck=lambda tg,d:(struct.pack(">I",len(d))+tg+d+struct.pack(">I",zlib.crc32(tg+d)&0xffffffff))
    open(fn,"wb").write(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",160*s,152*s,8,2,0,0,0))+ck(b"IDAT",zlib.compress(bytes(out),9))+ck(b"IEND",b""))
def ppm(p):
    b=open(p,"rb").read(); j=0; tk=[]
    while len(tk)<4:
        while b[j:j+1].isspace(): j+=1
        k=j
        while not b[k:k+1].isspace(): k+=1
        tk.append(b[j:k]); j=k
    return b[j+1:]
def run(cards,out):
    """한 번 켜서 여러 장을 돈다 — 설명면에서 A 두 번이면 목록으로 돌아온다."""
    script=["1200 -","8 B","180 -"]+["8 D","40 -"]*3+["8 B","240 -","8 B","180 -"]
    tags=[]; cur=0                                   # 목록 커서 위치(0부터)
    for n in cards:
        want=n-1
        dr=want//8-cur//8; dc=want%8-cur%8
        for _ in range(abs(dr)): script+=["8 "+("D" if dr>0 else "U"),"40 -"]
        for _ in range(abs(dc)): script+=["8 "+("R" if dc>0 else "L"),"40 -"]
        script+=["30 -","8 B","150 -"]; tags.append("f%03d"%n); script.append("!f%03d"%n)
        script+=["8 B","150 -"]; tags.append("d%03d"%n); script.append("!d%03d"%n)
        script+=["8 A","150 -"]                             # 설명에서 A 한 번이면 목록이다(앞면을 건너뛴다)
        cur=want
    t=tempfile.mkdtemp(); rom=os.path.join(t,"r.ngc"); shutil.copy(ROM,rom)
    io.open(os.path.join(t,"s.txt"),"w",encoding="utf-8",newline="\n").write("\n".join(script)+"\n")
    subprocess.run([RUN,CORE,rom,os.path.join(t,"s.txt"),os.path.join(t,"g")],capture_output=True,text=True,env=E)
    os.makedirs(out,exist_ok=True); n=0
    for tg in tags:
        p=os.path.join(t,"g_%s.ppm"%tg)
        if os.path.exists(p): png(ppm(p),"%s/%s.png"%(out,tg)); n+=1
    return n
if __name__=="__main__":
    a=int(sys.argv[1]); b=int(sys.argv[2])
    out=os.path.expanduser(sys.argv[3] if len(sys.argv)>3 else "~/ss2/tmp/cards/shots")
    print("찍은 장",run(list(range(a,b+1)),out))
