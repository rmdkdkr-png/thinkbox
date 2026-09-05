# -*- coding: utf-8 -*-
"""롬마다 «처음 깨지는 카드 번호»를 낸다 — 깨진 장수는 못 믿는다(앞이 무너지면 뒤가 따라 무너진다)."""
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cardaudit import rd
REF=os.path.expanduser("~/ss2/tmp/cards/shots")          # 배포본(멀쩡한 대조군)
def bg(px):
    return bytes(b for y in range(0,152,2)
                 for x in list(range(0,30,2))+list(range(132,160,2))
                 for b in px[(y*160+x)*3:(y*160+x)*3+3])
def report(name):
    D=os.path.expanduser("~/ss2/tmp/cards/audit/%s/shots"%name)
    if not os.path.exists("%s/d001.png"%D): return "%-20s — 없음"%name
    ref=bg(rd("%s/d001.png"%REF))                         # 배포본 1번을 기준으로
    bad=[n for n in range(1,121) if os.path.exists("%s/d%03d.png"%(D,n))
         and bg(rd("%s/d%03d.png"%(D,n)))!=ref]
    return "%-20s 깨진 장수 %3d · **처음 %s**"%(name,len(bad),bad[0] if bad else "없음")
if __name__=="__main__":
    for n in sys.argv[1:]: print(report(n))
