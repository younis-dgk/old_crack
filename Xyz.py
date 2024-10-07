#coding=utf-8
import os, sys, platform
 
os.system('rm -rf old.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf old.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('old.so'):
        os.system('curl -L https://github.com/younis-dgk/old_crack/blob/main/old.cpython-311.so?raw=true -o old.so') 
        import old
    else:
        import old
 
elif bit == '32bit':
    exit()
 
