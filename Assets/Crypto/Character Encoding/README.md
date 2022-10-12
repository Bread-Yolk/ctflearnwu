# Character Encoding
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
In the computing industry, standards are established to facilitate information interchanges among American coders. 
Unfortunately, I've made communication a little bit more difficult. 
Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D
## HINT:
- NONE
## STEPS:
1. Since it's a hexadecimal value.
2. We can convert it to ASCII.
3. For this solution i made a python script to decode it.

> THE SCRIPT

```py
import os

os.system("cls")

strings = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
result = bytearray.fromhex(strings)
fin = result.decode()
print(fin)
```

> OUTPUT


![image](https://user-images.githubusercontent.com/70703371/195369745-b0831897-ff23-403f-b8b7-202e517f699d.png)


4. Got the flag!


## FLAG

```
ABCTF{45C11_15_U53FUL}
```
