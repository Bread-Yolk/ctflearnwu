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


5. Awesome! 
