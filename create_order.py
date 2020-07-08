import binascii
import zlib
import json

# def crc(l1):
#     l2 = [l1[i: i+2] for i in range(0, len(l1), 2)]
#     print(l2)
#     l2 = map(lambda x: binascii.a2b_hex(x).decode('unicode_escape'), l2)
#     print(l2)
#     # l2 = map(lambda x: x.decode(), l2)
#     l1 = ''.join(l2)
#     c = zlib.crc32(l1.encode())
#     return hex(c)[2:]

def crc(l1):
    l2 = binascii.a2b_hex(l1)
    print(l2)
    c = zlib.crc32(l2)
    return hex(c)[2:]

def ordercreate(l1, l2, l3):
    return 'aa55' + l1 + '{:04x}'.format(int(len(l2)/2)) + l2 + l3 + '33cc'

a = crc('000200020001')
a = ordercreate('0002', '0001', a)
b = crc('000200020002')
b = ordercreate('0002', '0002', b)
c = crc('00020003000300')
c = ordercreate('0002', '000300', c)
d = crc('00020003000301')
d = ordercreate('0002', '000301', d)
# e = crc('0001000e0001000200000107e406130a0100')
# print(e)
f = crc('00010003000100')
f = ordercreate('0001', '000100', f)
order_dict = {}
order_dict['getMAC'] = a
order_dict['getPOWER'] = b
order_dict['getSTATE'] = c
order_dict['getSTATEagain'] = d
order_dict['stop'] = f

print(a)
print(b)
print(c)
print(d)
print(f)

# with open("order_dict.json", 'w') as f:
#     json.dump(order_dict, f)

