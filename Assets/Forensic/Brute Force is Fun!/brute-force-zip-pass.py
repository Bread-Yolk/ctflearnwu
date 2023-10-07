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
