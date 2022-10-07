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


![image](https://user-images.githubusercontent.com/70703371/194580316-206f5842-0192-4c63-b6c8-ef007d3ebc8c.png)


5. Open the `flag` directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194580397-96c7d8f5-e66d-4824-9a67-915788f30ffc.png)


6. Open the `hide` directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194580512-1669e6a9-5eaf-4c7e-84b9-8e094d0d50be.png)


7. Got the flag!


## FLAG

```
CTFlearn{gh0sbu5t3rs_4ever}
```

## LEARNING REFERENCES:

```
https://hackertarget.com/gobuster-tutorial/
```
