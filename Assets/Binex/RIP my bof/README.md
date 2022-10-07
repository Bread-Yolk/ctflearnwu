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
