# Phone
> Write-up author: jon-brandy
## DESCRIPTION:
My boss was calling me yesterday but I wasn't able to answer the phone. He left me an encoded message in the voicemail. 
There are a lot of weird sounds going on. I have to know what he wanted to tell me. Could you help me decode it? I bet it's something important.

Here is the audio file from my voicemail:

## HINT:
- NONE
## STEPS:
1. In this challenge we're given a .wav audio file.
2. Hearing the sound it's clear that this challenge required a **dtmf-decoder**.
3. I used the tool from this github --> `https://github.com/ribt/dtmf-decoder`.

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/c0c4c022-7c43-4f9a-a891-420736fdec07)


4. We need to parse it now, the remove all the numbers which are not `1` or `0` then separate it with `#`.
5. If you bum to a condition like this:

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/bc564d12-26ea-4e1b-8066-c8cbd21c1be1)


6. We need to analyze the pattern, so it's kinda guessy at this point. What I meant by pattern is, if you noticed some of the binaries which has **longer** length has another duplicate which has shorter length.
7. So compare it with them and remove double values.
8. BUT, if there's a case where there's no similiar binaries, hence try to remove and add the `0` number might help.

> RESULT

```
0000000100110110010000000#
0111110100011001010111110#
0100010101000101110100010#
0100010100110011110100010#
0100010111101011010100010#
0111110101110001010111110#
00000001010101001010000000#
1111111110100111011111111#
00011000111110111011010000#
1100001100001010010100110#
1010100101101100111000111#
000000111101010100001101001#
10000100010000111000111000#
0010001001101010100100000#
1110100011000010111100011#
1111111010011111101001010#
0000110010011010000001010#
1111111100000110011100110#
0000000111100000010101011#
0111110101001101011101011#
01000010101111111000001001#
0100010110100001000011100#
0100#
010111001001001011001#
0111110100011110010101001#
0000000101111110100000000#
```

> REVISED

```
0000000100110110010000000#
0111110100011001010111110#
0100010101000101110100010#
0100010100110011110100010#
0100010111101011010100010#
0111110101110001010111110#
0000000101010101010000000#
1111111110100111011111111#
0011000111110111011010000#
1100001100001010010100110#
1010100101101100111000111#
0000001111010100001101001#
1000010001000111000111000#
0010001001101010100100000#
1110100011000010111100011#
1111111010011111101001010#
0000110010011010000001010#
1111111100000110011100110#
0000000111100000010101011#
0111110101001101011101011#
0100010101111111000001001#
0100010110100001000011100#
0100010111001001001011001#
0111110100011110010101001#
0000000101111110100000000#
```

9. Then I used this template script to render it to barcode and scan it.

```py
from pyzbar import pyzbar
import numpy as np
import cv2
import os 
from pwn import *
# os.system('clear')

binaries = "0000000100110110010000000011111010001100101011111001000101010001011101000100100010100110011110100010010001011110101101010001001111101011100010101111100000000101010101010000000111111111010011101111111100110001111101110110100001100001100001010010100110101010010110110011100011100000011110101000011010011000010001000111000111000001000100110101010010000011101000110000101111000111111111010011111101001010000011001001101000000101011111111000001100111001100000000111100000010101011011111010100110101110101101000101011111110000010010100010110100001000011100010001011100100100101100101111101000111100101010010000000101111110100000000"
list = []
for i in binaries:
    if int(i) == 1:
        list.append(255)
    else:
        list.append(int(i))

image_render = np.array(list)
image_render = image_render.reshape(25,25).astype('float32') 
resized = cv2.resize(image_render, (36*10,37*10), interpolation = cv2.INTER_AREA)
cv2.imwrite('output.png',resized)

image_render_decode = cv2.imread("output.png")
barcodes = pyzbar.decode(image_render_decode)
print(barcodes)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image_render_decode, (x, y), (x + w, y + h), (0, 0, 255), 2)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image_render_decode, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    success("found {} barcode {}".format(barcodeType, barcodeData))
```

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/06225ded-816c-4cb6-bd38-6326e0a65fb5)


10. Got the flag!

## FLAG

```
CTFlearn{DTMF_1s_y0ur_fr13nd}
```
