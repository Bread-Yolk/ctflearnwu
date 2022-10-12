# BruXOR
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
There is a technique called bruteforce. Message: q{vpln'bH_varHuebcrqxetrHOXEj No key! Just brute .. brute .. brute ... :D
## HINT:
- NONE
## STEPS:
1. Simply paste the ciphertext to [cyberchef](https://gchq.github.io/CyberChef/#recipe=XOR_Brute_Force(1,100,0,'Standard',false,true,false,'')&input=cXt2cGxuJ2JIX3Zhckh1ZWJjcnF4ZXRySE9YRWo)
2. Based from the description, let's use `XOR Bruteforce` as the recipe.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195385000-7e4ccf6e-286b-41e2-a803-e9c472e624ec.png)


![image](https://user-images.githubusercontent.com/70703371/195385139-f25dc4d1-f6e6-4c8d-a34a-ea6035eab294.png)


3. Got the flag!


## FLAG

```
flag{y0u_Have_bruteforce_XOR}
```
