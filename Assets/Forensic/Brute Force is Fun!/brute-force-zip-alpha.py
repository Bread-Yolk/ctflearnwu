from zipfile import ZipFile
import itertools
import os 
from pwn import *

os.system('clear')

# Define the characters to use for generating the password
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# The password is: "ctflag*****" where * is an alphanumeric character.
password_length = 5
alphanumeric_combinations = itertools.product(characters, repeat=password_length)

with ZipFile('1926.zip') as zip:
    for combo in alphanumeric_combinations:
        password = 'ctflag' + ''.join(combo)
        try:
            zip.extractall(pwd=bytes(password, 'utf-8'))
            log.success(f'PASSWORD --> {password}')
        except:
            pass
