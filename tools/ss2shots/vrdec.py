# VRAM 덤프 해독 — 평면 지도/타일/팔레트를 읽어 화면을 다시 그린다
import os,struct,zlib
V=os.path.expanduser("~/ss2/tmp/vr")
def load(tag):
    d={}
    for k in ("char","scroll","pal","sprite","spritecol"): d[k]=open("%s/%s.%s"%(V,tag,k),"rb").read()
    return d
def cell(scroll,plane,r,c):
    o=(plane*2048)+((r*32+c)*2); v=scroll[o]|(scroll[o+1]<<8)
    return v&0x1FF, (v>>9)&1, (v>>10)&1, (v>>12)&0xF     # tile, hf, vf, pal(가정A)
def cellB(scroll,plane,r,c):
    o=(plane*2048)+((r*32+c)*2); b0,b1=scroll[o],scroll[o+1]
    return b0|((b1&1)<<8), (b1>>7)&1, (b1>>6)&1, (b1>>1)&0xF   # 가정B(내 옛 기록)
def pal(palram,idx,ci):
    o=idx*8+ci*2; v=palram[o]|(palram[o+1]<<8)
    r=(v>>8)&0xF; g=(v>>4)&0xF; b=v&0xF
    return (r*17,g*17,b*17)
def tilepix(char,t):
    o=t*16; out=[]
    for y in range(8):
        w=char[o+y*2]|(char[o+y*2+1]<<8); row=[]
        for x in range(8): row.append((w>>(14-2*x))&3)
        out.append(row)
    return out
