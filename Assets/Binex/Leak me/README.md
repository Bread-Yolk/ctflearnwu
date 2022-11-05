# Leak me
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
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


3. Check the `task` file first.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194568647-0176fe53-28ae-4e78-86e7-7823559f08fe.png)


![image](https://user-images.githubusercontent.com/70703371/194568758-0820270d-2000-4f14-b6ab-4dc3120ea570.png)


4. Since the file is not stripped, so we can see the functions names.
5. Anyway let's try to run the file using gdb.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194569285-4c9004d1-276c-4b45-9850-de354bf9f8bd.png)


6. Hmm.. let's analyze the code then.

> TASK.C

```c
#include <stdlib.h>
#include <stdio.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    char flag[64], buffer[64];

    FILE *f = fopen("./flag.txt", "rt");
    if (f == NULL) {
        puts("No flag.txt found, contact an admin");
        return 1;
    }

    fgets(flag, 64, f);      
    fclose(f);

    printf("What is your favorite format tag? ");
    fgets(buffer, sizeof(buffer), stdin);
    printf(buffer);

    return 0;
}

```

7. It seems we need to create file `flag.txt` first and let's type `FLAG{}` for the text inside.
8. Now let's run the file in gdb again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194570111-94b37b00-6117-4c2a-bf6d-af1ea2727600.png)


9. Since it asks us about format tag, i tried to input %x.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200119912-0d5c0715-4382-408b-9452-f2e92894fe5a.png)


![image](https://user-images.githubusercontent.com/70703371/200119930-86dd15f1-4fd2-411c-9a80-739865718abf.png)


10. Just a random decimal value.
11. Then i tried to input 20 %x. -> %x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200120066-60f3b040-9b75-4b39-b017-972d82602a6d.png)


12. Hmm noticed there's one 

