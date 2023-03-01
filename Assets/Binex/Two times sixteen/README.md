# Two times sixteen
> Write-up author: jon-brandy
## DESCRIPTION:
Your task is simple - call the function print_flag. It is guarded by a couple of ifs - good luck in defeating them.

nc rivit.dev 10000

## HINT:
- NONE
## STEPS:
1. After unzipping the file, we got 2 files -> binary and it's source code.
2. First, check the binary type and it's protections.

> 64 bit, not stripped

![image](https://user-images.githubusercontent.com/70703371/222120384-206e6d8a-e9f3-4f00-bbbd-0274e24899a4.png)


> VULN -> Partial RELRO, No Canary Found, No PIE

![image](https://user-images.githubusercontent.com/70703371/222120463-fff58f63-7b91-421c-b426-6be13eb20e0e.png)


3. No need to decompile the binary, because we have the source code, let's analyze it then.

> THE SOURCE CODE

```c
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void print_flag(int p1, unsigned int p2){
    printf("You passed the following arguments:\n");
    printf("p1 = %d\n", p1);
    printf("p2 = 0x%X\n", p2);

    FILE *f = NULL;
    char flag[64];

    if(p1 == -1337){
        f = fopen("/flag.txt", "rt");
        if (f == NULL){
            puts("Could not open a flag file! Contact an admin.");
            return;
        }
    }

    if(p2 == 0xC0FFEE){
        fgets(flag, sizeof(flag), f);
        puts(flag);
    }

    if(f != NULL){
        fclose(f);
    }
}

void vuln(){
    puts("Do you want to say something?");
    char buf[32];
    read(STDIN_FILENO, buf, 64);

    print_flag(-1, 2);
}

int main(int argc, char *argv[]){
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    vuln();

    return 0;
}

```

4. Notice there's a bufferoverflow at the **vuln()** function, where the buf variables accepts 64 bytes but it only has 32 bytes as it's buffer.

> VULN()

```c
void vuln(){
    puts("Do you want to say something?");
    char buf[32];
    read(STDIN_FILENO, buf, 64);

    print_flag(-1, 2);
}
```

5. Hence, we can control the **RIP** and passing arguments to the **print_flag** function. 
6. Analyzing the **print_flag** function, it seems we need to pass `-1337` as the first argument, then `0xC0FEE` as the second argument.
7. Let's get the **RIP** offset before crafting the exploit.

> Utilized the leaked RSP value -> got 40 bytes as the offset

![image](https://user-images.githubusercontent.com/70703371/222122233-23d0d443-74a5-47b1-a8d3-75cae4943816.png)'


8. Remembering it's in 64 bit, hence we need **pop rdi** and **pop rsi** for passing the 1st arg & the 2nd arg.

> pop rdi -> 

