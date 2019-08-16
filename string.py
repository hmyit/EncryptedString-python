#encypted string with XPoly Engine
strHelloWorld = [
    0x4c, 0x30, 0x2a, 0x2b, 0x29, 0x6d, 0x7a, 0x44,
    0x2d, 0x2b, 0x32, 0x3b, 0x7f, 0xa1
]

for XceMz in range(14):
 WaXPq = strHelloWorld[XceMz]
 WaXPq -= XceMz
 WaXPq = -WaXPq
 WaXPq += 0x94
 strHelloWorld[XceMz] = WaXPq

s = ''.join(chr(WaXPq & 0xff) for WaXPq in strHelloWorld)

del WaXPq, XceMz

print(s)
