import pickle,os,struct,zlib,hashlib,sys
def sig(px):
    idx=range(0,len(px),3*7); blk=wht=0
    for i in idx:
        r,g,b=px[i],px[i+1],px[i+2]
        if r<40 and g<40 and b<40: blk+=1
        elif r>200 and g>200 and b>200: wht+=1
    m=len(list(idx)); return blk*100//m, wht*100//m
def png(px,fn,s=1):
    out=bytearray()
    for y in range(152):
        line=bytearray()
        for x in range(160): line+=px[(y*160+x)*3:(y*160+x)*3+3]*s
        for _ in range(s): out+=b"\x00"+bytes(line)
    ck=lambda tg,d:(struct.pack(">I",len(d))+tg+d+struct.pack(">I",zlib.crc32(tg+d)&0xffffffff))
    open(fn,"wb").write(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",160*s,152*s,8,2,0,0,0))+ck(b"IDAT",zlib.compress(bytes(out),9))+ck(b"IEND",b""))
def sheet(sel,fn,cols=8):
    rows=(len(sel)+cols-1)//cols; out=bytearray()
    for rr in range(rows):
        for y in range(152):
            line=bytearray()
            for c in range(cols):
                i=rr*cols+c; line+=sel[i][1][y*480:(y+1)*480] if i<len(sel) else bytes(480)
            out+=b"\x00"+bytes(line)
    ck=lambda tg,d:(struct.pack(">I",len(d))+tg+d+struct.pack(">I",zlib.crc32(tg+d)&0xffffffff))
    open(fn,"wb").write(b"\x89PNG\r\n\x1a\n"+ck(b"IHDR",struct.pack(">IIBBBBB",160*cols,152*rows,8,2,0,0,0))+ck(b"IDAT",zlib.compress(bytes(out),9))+ck(b"IEND",b""))
if __name__=="__main__":
    k=int(sys.argv[1]); F=pickle.load(open(os.path.expanduser("~/ss2/tmp/end/k%02d.pkl"%k),"rb"))
    prev=None
    for i,(idx,px) in enumerate(F):
        b,w=sig(px)
        print("%3d 검%3d 흰%3d"%(idx,b,w),end="  " if i%6!=5 else "\n")
    print()
    for i in range(0,len(F),48): sheet(F[i:i+48],"e%02d_%02d.png"%(k,i//48))

def isend(px):
    """엔딩 글 페이지인가 — 좌우 갈색 체크 테두리 + 가운데는 거의 검다."""
    br=0
    for y in range(0,152,2):
        for x in list(range(0,14,2))+list(range(146,160,2)):
            i=(y*160+x)*3; r,g,b=px[i],px[i+1],px[i+2]
            if r>90 and 40<g<130 and b<90: br+=1
    dk=0; n=0
    for y in range(0,152,3):
        for x in range(24,136,3):
            i=(y*160+x)*3; n+=1
            if px[i]<40 and px[i+1]<40 and px[i+2]<40: dk+=1
    return br>60 and dk*100//n>80
