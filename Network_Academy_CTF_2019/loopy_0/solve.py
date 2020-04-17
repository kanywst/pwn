from pwn import *

e = ELF('./loopy-0')
p = process('./loopy-0')

p.sendline('A*10')
print p.recv()
p.interactive()