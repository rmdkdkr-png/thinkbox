# -*- coding: utf-8 -*-
"""IPS 검산 — 본부 몫. 1-f7 도구와 «따로 짠» 적용기로 입혀서 결과 해시를 본다.
   같은 코드로 만들고 같은 코드로 검사하면 둘 다 틀려도 통과한다."""
import io, os, sys, hashlib

def apply_ips(rom: bytes, ips: bytes) -> bytes:
    assert ips[:5] == b'PATCH', 'IPS 머리가 아니다'
    out = bytearray(rom)
    p = 5
    n_rec = 0
    while True:
        if ips[p:p + 3] == b'EOF':
            p += 3
            break
        off = (ips[p] << 16) | (ips[p + 1] << 8) | ips[p + 2]; p += 3
        size = (ips[p] << 8) | ips[p + 1]; p += 2
        if size == 0:                       # RLE
            rle = (ips[p] << 8) | ips[p + 1]; p += 2
            val = ips[p]; p += 1
            if off + rle > len(out): out.extend(b'\x00' * (off + rle - len(out)))
            out[off:off + rle] = bytes([val]) * rle
        else:
            data = ips[p:p + size]; p += size
            if off + size > len(out): out.extend(b'\x00' * (off + size - len(out)))
            out[off:off + size] = data
        n_rec += 1
    tail = len(ips) - p
    return bytes(out), n_rec, tail

PRIS = os.path.expanduser("~/ss2/rom/pristine/Samurai Shodown! 2 (JUE) [!].ngc")
R = os.path.expanduser('~/ss2/work_lang/v10/release_final/')
rom = io.open(PRIS, 'rb').read()
print('순정 md5', hashlib.md5(rom).hexdigest(), len(rom), 'B')
print('-' * 72)

cases = sys.argv[1:] or [
    (R + 'cand_SS2_Korean_v1.0.ips', R + 'cards_v9_final.ngc'),
    (R + 'cand_SS2_Korean_v1.0_allcards.ips', R + 'cards_v9_final_allcards.ngc'),
]
if cases and isinstance(cases[0], str):
    cases = [(cases[i], cases[i + 1]) for i in range(0, len(cases), 2)]

for ips_path, want_path in cases:
    ips = io.open(os.path.expanduser(ips_path), 'rb').read()
    want = io.open(os.path.expanduser(want_path), 'rb').read()
    got, n_rec, tail = apply_ips(rom, ips)
    same = hashlib.md5(got).hexdigest() == hashlib.md5(want).hexdigest()
    print('%s' % os.path.basename(ips_path))
    print('   기록 %d개 · 꼬리 여분 %d B · IPS md5 %s' % (n_rec, tail, hashlib.md5(ips).hexdigest()))
    print('   입힌 결과 %s' % hashlib.md5(got).hexdigest())
    print('   기대한 롬 %s' % hashlib.md5(want).hexdigest())
    print('   %s' % ('✔ 같다' if same else '✘ 다르다'))
    if not same:
        d = [i for i in range(len(want)) if got[i] != want[i]]
        print('   다른 바이트 %d개 · 첫 자리 0x%06X' % (len(d), d[0]))
    print()
