import binascii
import ipaddress


ADDRESSES = [
    '10.9.0.6',
    '45.77.99.61',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]


for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print('IP version:', addr.version)
    print('is private:', addr.is_private)
    print('Packed form:', binascii.hexlify(addr.packed))
    print('Integer:', int(addr))
    print()
