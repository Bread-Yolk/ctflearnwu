# MountainMan
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Don't be fooled by two 0xffd9 markers. xor is your friend.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/16f496927f7de847e9cb77d0a93510853aeb2643/Assets/Forensic/MountainMan/MountainMan.jpg)

## HINT:
- NONE

## STEPS:
1. First, download the file given.
2. Based from the description, we may use **exiftool** to find the clue given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195990881-3e06925b-8389-496f-8eb3-0d5e1e7ac620.png)


3. At the bottom, generally there is only 1 0xffd9, which represents the End Of Image (EOI).
4. Let's copy the hexadecimal value right next from the FF D9.

> COPIED VALUE

```
88 9F 8D A7 AE AA B9 A5 B0 9E A9 BE A5 BF BE 94 B9 FB A8 A0 FE B6 FF D9
```

5. For this solution, i made a python script to decode it.

> SCRIPT

```py
```
