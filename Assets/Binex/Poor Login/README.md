# Poor Login
> Write-up author: jon-brandy
## DESCRIPTION:
Heap pwning can be easy right? Here's something to look at.

nc thekidofarcrania.com 13226

## HINT:
- NONE
## STEPS:
1. In this challenge we're given a 64 bit binary, dynamically linked, and not stripped.

```
┌──(brandy㉿bread-yolk)-[~/Downloads/ctflearn/poor-login/pwn-login]
└─$ file login       
login: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=304e214a790bd6fcd1ae83aa2dfd0a9cf7c8462c, not stripped
```

> BINARY PROTECTIONS

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/e898d136-c65d-4364-b696-52c0764df6e5)


2. We're given the source code, but somehow for me, I still need to decompile it to understand more about how bytes allocated on the heap and what computer reads as.
3. Reviewing the source code, the vuln is quite straight-forward, it's **Use-After-Free**.
4. We can see that there's 5 menu we can use here:

