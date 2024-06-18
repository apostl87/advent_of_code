if ip == 0:
    r5 = 0
    ip = 6
if ip == 6:
    if r5 >= 0xffff:
        r3 = r5
    else:
        r3 = r5 + 0xffff
    r5 = 9010242
    ip = 8
if ip == 8:
    r1 = r3 % 0x100
    r5 = (((r1+r5)) % 0x1000000) * 65899) % 0x1000000
    if r3 < 256:
        ip = 28
    else:
        r1 = 0
        ip = 18
if ip == 18:
    r4 = (r1 + 1)*256
    if r4 > r3:
        r3 = r1
        ip = 8
    else:
        r1 += 1
        ip = 18
if ip == 28:
    if r5 == r0:
        print(r0)
    else:
        r1 = 0
        ip = 6

