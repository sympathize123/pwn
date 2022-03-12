from pwn import *
r = ssh('random', 'pwnable.kr', 2222, 'guest')
b = bytes(a ^ b for a, b in zip(p32(1804289383), p32(0xdeadbeef)))
a = int.from_bytes(b, "little")
print(a)
fd = r.process(['./random'])
fd.sendline(bytes(str(a), 'ascii'))
print(fd.recvall())
