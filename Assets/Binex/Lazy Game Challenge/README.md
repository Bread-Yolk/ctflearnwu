# Lazy Game Challenge
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I found an interesting game made by some guy named "John_123". It is some betting game. 
I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at: `nc thekidofarcrania.com 10001`
## HINT:
- NONE
## STEPS:
1. First, open the netcat given.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/193379006-0c1d2a94-50d3-4a35-b3cf-4fbd62f3e396.png)

2. Enter `y`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193379028-df060f2c-45ea-4bbd-9498-e7479fe2c18b.png)


3. So we have 10 chances to guess it and we need to bet the money.
4. The logic here, if we can input the **minus** integer as our bet, it means we just have to guess it randomly until we don't have any chances left.
5. Let's see if we can input **minus** value as the input.

> NOTES

```
Result = Balance - (what u bet).
IF input == minus value, then

THE GOALS
=========

Result = 500 - ( - 1000000)
Result = 500 + 1000000
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193379105-eb2bb9a8-7f1b-4140-aa97-5ec062fbe8ee.png)


6. Turns out we can, means this is just simple **Binary Exploitation** challenge.
7. Now, let's guess any random number or string etc, until you don't have any guesses anymore.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193379222-698f2718-8ce8-432f-adbc-7545c816ef71.png)


8. Got the flag!

```
CTFlearn{d9029a08c55b936cbc9a30_i_wish_real_betting_games_were_like_this!}
```
