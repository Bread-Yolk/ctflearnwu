# Positive challenge
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I made sure that you couldn't get a negative value, I also forced only positive numbers even if you give negative.

`nc rivit.dev 10010`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/f3dc1761659066a2e55f8df58f36dc441b5ee20c/Assets/Binex/Positive%20challenge/task.tar.gz)

## HINT:
- NONE
## STEPS:
1. First, download the given file.
2. Next, extract it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739676-d6b736ba-47a8-492e-8520-b18ce5be01cd.png)


3. Let's run the netcat first.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739710-b34368e0-74a0-401a-bae4-2dbd32f4b4fd.png)


4. Hmm.. We can't add negative value here.
5. Let's analyze the code then.

> TASK.C

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

6. **%hd** is new to me.
7. So i did small research for that.

> SMALL RESEARCH - STACK OVERFLOW

![image](https://user-images.githubusercontent.com/70703371/194739757-cf5c1489-52e3-4f10-9298-858f9752929d.png)


8. 
