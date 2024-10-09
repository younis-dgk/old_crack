import os,re,sys,platform

os.system('rm -rf old.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf old.so')
except:
    pass
 
bit = platform.architecture()[0]
if bit == '64bit':
    import old
elif bit == '32bit':
    print(f"\033[1;91m Sorry Baby 32 Bit Not Supported .... ");exit() 
 
