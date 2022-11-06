# Suspecious message 
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Hello! My friend Fari send me this suspecious message: 'MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}' and photo.png. Help me decrypt this! 

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/1fc643b2370ab20d4fb984fe84fc812208b8269c/Assets/Crypto/Suspecious%20message/photo.png)

## HINT:
- NONE
## STEPS:
1. First, download the file given.

> PHOTO.PNG

![image](https://user-images.githubusercontent.com/70703371/200157330-362191e8-92ff-4a23-83f6-67f4c6521b14.png)


2. Based from image given, we can conclude the ciphertext given is **playfair ciphertext**.

> PLAYFAIR

![image](https://user-images.githubusercontent.com/70703371/200157429-4303eb98-a43d-4b3c-a183-5db474d63ed4.png)


```
The Playfair cipher uses a 5×5 grid of letters, and encrypts a message by breaking the text into pairs of letters and swapping them according to their positions in a rectangle within that grid: "HI" becomes "BM".
```


3. For this solution, i used [this](https://www.boxentriq.com/code-breaking/playfair-cipher) online decryptor.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200157558-4bfa9f66-1711-4e17-b6ca-b808388391bb.png)


4. Got the flag!

## FLAG

```
CTFLEARN{PL4YF41R_1S_C00L_C1PHERRRR}
```
