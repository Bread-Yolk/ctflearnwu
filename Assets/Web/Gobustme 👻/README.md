# Gobustme 👻
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Some ghosts made this site 👻, it's a little spooky but theres a bunch of stuff hidden around. 

gobustme.ctflearn.com

## HINT:
- NONE

## STEPS:
1. First, open the link given.
2. Scroll down to the bottom.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194578634-43d39523-06b4-4de1-8d38-25e2fa2d8675.png)


3. Based from this lyrics, i think we may have to use a tools called `gobuster`.
4. Let's use `gobuster`. 

> COMMAND

```sh
gobuster dir -u https://gobustme.ctflearn.com/ -w common.txt
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194579893-1b40e55a-e3e9-4f06-bb82-1796e82e94bc.png)


5. 
