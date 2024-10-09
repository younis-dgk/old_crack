#coding=utf-8
import os, sys, platform
os.system("git pull")
os.system('rm -rf old64.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf old64.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('old64.so'):
        os.system('curl -L https://github.com/younis-dgk/old_crack/blob/main/old64.cpython-312.so?raw=true -o old64.so') 
        import old64
    else:
        import old64
 
elif bit == '32bit':
    print("\033[1;90m [\033[1;91m Sorry Baby 32 Bit Not Supported! 🥺💔\033[1;90m]");exit()
 
 
 
 
