# Positive challenge
> Write-up author: jon-brandy
## DESCRIPTION:
I made sure that you couldn't get a negative value, I also forced only positive numbers even if you give negative.

nc rivit.dev 10010

## HINT:
- NONE
## STEPS:
1. First, download the source code given.

> THE SOURCE CODE

```c
#include <stdlib.h>
#include <stdio.h>

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

	short acc = 0;
	short n;
	while(acc >= 0){
		printf("acc = %d\n", acc);
		printf("Enter a number to add: ");
		if(scanf("%hd", &n) != 1){
			while(getchar() != '\n');
			puts("Invalid value");
			continue;
		}

		if(n < 0){
			n = abs(n);
		}

		n %= 100;
		acc += n;
		acc %= 100;
	}

	system("cat ./flag.txt");
}

```

2. Based from the code, we know the vuln is at the scanf operation where it takes **short integer** and stored it inside the **n** variable.
3. Remembering the short integer can only store values within the range of -32,768 to 32,767.
4. Hence to trigger the `system()` , let's enter the number of 32768.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/221827691-909d6965-a541-4cac-9c7f-be8e71ff52c8.png)


5. Got the flag!

## FLAG

```
CTFlearn{n0t_s0_p0s1t1v3_4t_4ll}
```
