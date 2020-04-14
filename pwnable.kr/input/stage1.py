import subprocess
import os

# stage 1
args = ["A" for i in range(100)]

args[ord("A")] = ""
args[ord("B")] = "\x20\x0a\x0d"

# s = subprocess.call(["/home/kanye/pwnable.kr/input/input"]+args[1:])

# stage 2
with open("stdin.txt","w") as f:
	f.write("\x00\x0a\x00\xff")
with open("stderr.txt","w") as f:
	f.write("\x00\x0a\x02\xff")

# stage 3
os.environ["\xde\xad\xbe\xef"] = "\xca\xfe\xba\xbe"

s = subprocess.call(["/home/kanye/pwnable.kr/input/input"]+args[1:],stdin=open("stdin.txt","r"),stderr=open("stderr.txt","r"))