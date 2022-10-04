# Simple bof
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Want to learn the hacker's secret? Try to smash this buffer!

You need guidance? Look no further than to Mr. Liveoverflow. He puts out nice videos you should look if you haven't already

`nc thekidofarcrania.com 35235`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/defef2a071ebf4736bf939098b307008378d6b8b/Assets/Binex/Simple%20bof/bof.c)

## HINT:
- NONE
## STEPS:
1. First, download the `.c` file given.
2. Next, let's run the netcat first.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193816845-173c0654-c109-4d73-951c-46593ceb105d.png)


3. Looks like it just a simple bufferoverflow.
4. Let's input any length of A's.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193816971-cc951b12-bec6-4250-b368-8920ab600b48.png)


5. It said we overflowed too much.
6. Let's analyze the source code then.

> BOF.C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Defined in a separate source file for simplicity.
void init_visualize(char* buff);
void visualize(char* buff);
void safeguard();

void print_flag();

void vuln() {
  char padding[16];
  char buff[32];
  int notsecret = 0xffffff00;
  int secret = 0xdeadbeef;

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Zero-out the padding.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 

  // Check if secret has changed.
  if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
    return;
  } else if (notsecret != 0xffffff00) {
    puts("Uhmm... maybe you overflowed too much. Try deleting a few characters.");
  } else if (secret != 0xdeadbeef) {
    puts("Wow you overflowed the secret value! Now try controlling the value of it!");
  } else {
    puts("Maybe you haven't overflowed enough characters? Try again?");
  }

  exit(0);
}

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  safeguard();
  vuln();
}

```

7. 

