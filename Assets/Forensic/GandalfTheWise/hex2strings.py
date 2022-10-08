import os

os.system("clear")

strings = "4354466c6561726e7b47616e64616c662e42696c626f42616767696e737d"
result = bytearray.fromhex(strings)
fin = result.decode()
print(fin)
