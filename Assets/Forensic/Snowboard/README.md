# Snowboard
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Find the flag in the jpeg file. Good Luck!

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/3a595dab2b8f3c1970096f4afde084fa862f3369/Assets/Forensic/Snowboard/Snowboard.jpg)

## HINT:
- NONE

## STEPS:
1. First, download the file given.
2. Anyway let's check the file tyoe.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193033079-15666475-1a1d-4313-b497-050f9cae08d7.png)


3. I thought this must be the flag. But it's not.
4. But notice, there's a **base64** text, let's decode it.

```
Q1RGbGVhcm57U2tpQmFuZmZ9Cg==
```

![image](https://user-images.githubusercontent.com/70703371/193033910-3e4b0864-d2ec-41d6-9b45-cff97bb67606.png)


5. We got the flag!

```
CTFlearn{SkiBanff}
```
