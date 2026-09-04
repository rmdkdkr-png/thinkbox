#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PPM 여러 장을 한 판으로 붙여 PNG 로 낸다 (눈으로 훑을 때 쓴다)."""
import glob, os, struct, sys, zlib

def readppm(p):
    d=open(p,'rb').read()
    assert d[:2]==b'P6'
    i=2; f=[]
    while len(f)<3:
        while d[i] in b' \t\r\n': i+=1
        if d[i:i+1]==b'#':
            while d[i] not in b'\r\n': i+=1
            continue
        j=i
        while d[j] not in b' \t\r\n': j+=1
        f.append(int(d[i:j])); i=j
    i+=1
    w,h,_=f
    return w,h,d[i:i+w*h*3]

def png(path,w,h,rgb):
    raw=b''.join(b'\x00'+rgb[y*w*3:(y+1)*w*3] for y in range(h))
    def ch(t,b): 
        c=t+b; return struct.pack('>I',len(b))+c+struct.pack('>I',zlib.crc32(c))
    open(path,'wb').write(b'\x89PNG\r\n\x1a\n'
        +ch(b'IHDR',struct.pack('>IIBBBBB',w,h,8,2,0,0,0))
        +ch(b'IDAT',zlib.compress(raw,9))+ch(b'IEND',b''))

files=sorted(sys.argv[2:])
cols=int(os.environ.get('COLS','5'))
ims=[readppm(p) for p in files]
tw=max(i[0] for i in ims); th=max(i[1] for i in ims)
rows=(len(ims)+cols-1)//cols
W,H=tw*cols,th*rows
buf=bytearray(W*H*3)
for k,(w,h,d) in enumerate(ims):
    ox,oy=(k%cols)*tw,(k//cols)*th
    for y in range(h):
        o=((oy+y)*W+ox)*3
        buf[o:o+w*3]=d[y*w*3:(y+1)*w*3]
png(sys.argv[1],W,H,bytes(buf))
print(sys.argv[1],W,H,len(ims))
