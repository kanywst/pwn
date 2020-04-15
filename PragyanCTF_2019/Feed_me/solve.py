from pwn import *

e = ELF('./challenge1')
p = process('./challenge1')

print p.recvuntil('\n')
var1 = int(p.recvuntil(' ;').rstrip(';'))
print var1
var2 = int(p.recvuntil(';').rstrip(' ; '))
print var2
var3 = int(p.recvuntil(';').rstrip(';'))
print var3

var4 = (var1+var3-var2)/2
var5 = str(var1 - var4)
var6 = str(var3 - var4)
var4 = str(var4)

payload = var4
payload += '-'*(10-len(var4))
payload += var5
payload += '-'*(10-len(var5))
payload += var6
payload += '-'*(10-len(var6))

p.sendline(payload)
p.interactive()
print p.recv()