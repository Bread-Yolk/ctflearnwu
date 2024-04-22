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


