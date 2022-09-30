# GandalfTheWise
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/193060899bc1cf8d4ff839bc8f33929fdc106b0c/Assets/Forensic/GandalfTheWise/Gandalf.jpg)

## HINT:
- NONE
## STEPS:
1. First, download the file first.
2. Next, use exiftool to see are there any hidden comments or clues.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193185035-b2b09f1e-56bf-43e6-a55d-0acd7363ce6e.png)


3. The comment value seems like a base64 text.
4. Decode it.

![image](https://user-images.githubusercontent.com/70703371/193185119-b04fede4-8801-490e-973f-1c95a10a8343.png)


5. Turns out it's an incorrect flag.
6. Hmm..
7. Let's run **file**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193186517-093ee8a9-e1f2-4d01-b5b8-ffd37c64ac39.png)

8. Turns out there's more than one comments.
9. When i tried to strings it.

![image](https://user-images.githubusercontent.com/70703371/193187020-89f517f0-e0ac-4911-9cb0-2b19c0d1ad91.png)


10. Turns out the 3 ciphertext has `+` as their prefix, which lead to a XOR ciphertext.
11. The first one should be base64 because we decode it correctly last time, and it has the `==` postfix.
12. What comes to my mind is we could use  `XOR calculator`.
13. Convert these two, to hex value:

```
+xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p
+h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU
```

> CONVERT TO HEX VALUE USING CYBERCHEF

```
2b 78 44 36 6b 66 4f 32 55 72 45 35 53 6e 4c 51 36 57 67 45 53 4b 34 6b 76 44 2f 59 2f 72 44 4a 50 58 4e 55 34 35 6b 2f 70
```

```
2b 68 32 72 69 45 49 6a 31 33 69 41 70 32 39 56 55 50 6d 42 2b 54 61 64 74 5a 70 70 64 77 33 41 75 4f 37 4a 52 69 44 79 55
```

14. Now open [XOR](https://xor.pw/) calculator and paste the hex value there.

> ![image](https://user-images.githubusercontent.com/70703371/193187552-4c6a8b73-a2a7-4517-aa70-f935a386b9f6.png)


15. Now press the `calculate XOR` button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193187671-7ebec530-e210-49d0-b28e-30cdadacaac8.png)


```
1076440223065864412c74235c750763070a07781f550f021e5f294b05770b2517791f665c2f5625
```

16. Somehow when i tried do convert it to strings, it gave us weird result.
17. Maybe the other 2 are the base64 text too, so the `+` just a deception.
18. Let's try convert it to hex from base64.

```
c4 3e a4 7c ed 94 ac 4e 52 9c b4 3a 5a 01 12 2b 89 2f 0f f6 3f ac 32 4f 5c d5 38 e6 4f e9
```

```
87 6a e2 10 88 f5 de 20 29 db d5 54 3e 60 7e 4d a7 6d 66 9a 5d c3 70 2e 3b b2 51 88 3c 94
```

19. Now, paste all of them to the  XOR calculator again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193188498-30a6b8f3-52d9-4e3a-a5dc-134b2f296cd0.png)


```
4354466c6561726e7b47616e64616c662e42696c626f42616767696e737d
```

20. For this solution i made simple python script to convert it.

```py
import os

os.system("clear")

strings = "4354466c6561726e7b47616e64616c662e42696c626f42616767696e737d"
result = bytearray.fromhex(strings)
fin = result.decode()
print(fin)
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/193189197-2bb95318-4561-4afb-8b53-a89c9c801e01.png)


21. Finally, we got the flag!


## FLAG

```
CTFlearn{Gandalf.BilboBaggins}
```
