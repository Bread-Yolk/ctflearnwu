# Smiling ASCII
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Find the flag on the smiling face.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/9ecc83c3deca81982d7d66f27be4f61b348b13b7/Assets/Forensic/Smiling%20ASCII/smiling.png)

## HINT:
- NONE

## STEPS:
1. First, download the image given.
2. Next, let's **strings** the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196392385-dd75ce3d-bfbb-4f50-8ce2-7658bec407d7.png)


3. Looks like it's a **base64** encoded text, decode it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196392518-ef86e49b-78af-4e0f-80d6-858c62c2d3d2.png)


4. Since it's a `.png` file, we can use `zsteg` to see any hidden text inside the image.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196393862-51d0ba07-f41c-49cd-8466-c7124854d26a.png)


5. Got nothing.
6. But based from the first clue we got, we may have to try all known methods.
7. Simply add `-a`.

> ZSTEG

![image](https://user-images.githubusercontent.com/70703371/196394088-d4297d2e-c3d8-43ec-9f60-4bd468de191f.png)


8. Got the flag!

## FLAG

```
CTFlearn{ascii_pixel_flag}
```
