# Domain name resolver
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Check IP of your favorite domain.

`nc rivit.dev 10004`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/219c3f872ee92e567d29e124b0c63dbaf5d44da4/Assets/Binex/Domain%20name%20resolver/task.tar.gz)

## HINT:
- NONE
## STEPS:
1. First, check the binary type and it's protections.

> 64 bit, not stripped

![image](https://user-images.githubusercontent.com/70703371/221830544-a849ccf1-34b5-4f8a-aa48-9abf06bc8ab6.png)


> ALL ENABLED

![image](https://user-images.githubusercontent.com/70703371/221830710-5053a7cd-7430-4a7e-90f7-52eb9be53892.png)


2. Let's decompile the binary then.

> main()

![image](https://user-images.githubusercontent.com/70703371/221830800-8d2ee7a0-47fb-46f0-bc87-a1fd9fcfa5f3.png)


3. Analyzing the main function we know that the input is not sanitized.

![image](https://user-images.githubusercontent.com/70703371/221831239-f6b386ba-265a-42f5-acc0-eb9789ad7236.png)


4. The program use the `system` call and use our input as it's argument/param.
5. Hence we can utilize it with input the strings `;cat flag.txt`.
6. This vuln commonly known as **command injection**.

> WHY WE NEED SEMICOLON?

```
The semicolon character (;) is commonly used in command injection attacks to concatenate multiple commands in a single line. 
In the context of this code, if an attacker inputs a semicolon followed by a command, the system() function will execute both 
the original command (generated using snprintf()), as well as the injected command concatenated by the semicolon.
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/221832156-203c62a0-245d-43e2-aced-816981a14b8c.png)


7. Got the flag!

## FLAG

```
CTFlearn{1s_c0mm4nd_1nj3ct10n_4_th1ng?}
```
