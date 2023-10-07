# Brute Force is Fun! 
> Write-up author: jon-brandy
## DESCRIPTION:
You'll need Brute Force to solve this. Knowing Python should help too. Oh! And Base64 encryption of course! Find the flag!

https://mega.nz/#!vf43RCyC!NNpuYjB3d-gevhsHXefwAAAmzk4tJHxUZr0GnrSDI_c Hash: e82a4b4a0386d5232d52337f36d2ab73
## HINT:
- NONE
## STEPS:
1. In this challenge we're given a .jpg file which embedded with several directories.
2. Extract those with binwalk shall resulting to this:

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/67611508-875f-4d1f-b983-ca14c2eb6850)


3. Inside the `folders` directory lies another directory again within it.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/94085814-de7d-497e-9189-7d12788ab484)


4. Also some of them is empty.
5. To filter it simply run this bash comamnd --> `find . -type d -empty -delete`.

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/e918c8c5-7507-4626-a1ee-db63f415ec5d)


6. Only one directory is not empty.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/7fa22b5d-74de-4069-8d67-50f12644f1c3)


7. Quite simple, it discloses the first part of the password and we need to bruteforce the rest.

> WHERE TO USE THE PASS

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/a9e49b7b-e2f4-4998-81de-23708c40c751)


8. Great! To get the full pass, I used python script.

> SCRIPT

```py
from zipfile import ZipFile
from string import digits
import itertools
import os 
from pwn import *

os.system('clear')

# The password is: "ctflag*****" where * is a number.
digit_to_guess = itertools.product(digits, repeat=5)
with ZipFile('1926.zip') as zip:
    for i in digit_to_guess:
        i = ''.join(i)
        password = 'ctflag'+i
        try:
            zip.extractall(pwd=bytes(password, 'utf-8'))
            log.success(f'PASSWORD --> {password}')
        except:
            pass
```


> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/bea20c46-e949-42d7-8005-d114a1d6072a)


9. Using the password to unzip the 1926.zip file shall resulting to a .txt file.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/251b4be9-3f06-4023-aa7b-b5902532b7e9)


10. Decode the base64 and we got the flag!

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/6785355e-8da3-47e1-8d02-0399e36c2213)


## FLAG

```
FLAG{may_the_brute_force_be_with_you}
```
