f = open('TheMessage.txt', 'r').read()
strings = ""

for i in f:
    if ord(i) == 32:
        strings += "0"
    else:
        strings += "1"

print(strings)
