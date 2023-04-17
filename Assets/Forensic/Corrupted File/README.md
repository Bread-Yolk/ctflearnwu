# Corrupted File
> Write-up author: vreshco
## DESCRIPTION:
Help! I can't open this file. Something to do with the file header… Whatever that is. https://mega.nz/#!aKwGFARR!rS60DdUh8-jHMac572TSsdsANClqEsl9PD2sGl-SyDk
## HINT:
- NONE
## STEPS:
1. Given a corrupted gif file.
2. Based from the description, it's only tampered at the header file.
3. Did a small outsource about gif header and got this:

![image](https://user-images.githubusercontent.com/70703371/232398211-6c246ff8-058a-4abb-a9b8-b621e9bf8734.png)


4. We just need to change the first 4 chunks.

> RESULT -> Change it with **bless**.

![image](https://user-images.githubusercontent.com/70703371/232398372-112c99bc-aa72-4e83-9e7a-c54c9c1e0b76.png)


![image](https://user-images.githubusercontent.com/70703371/232398432-8d8a6620-c68f-4b1f-8134-0391bb3f7c25.png)


5. Successfully recovered the gif file, we can check the text frame by frame using [this](https://ezgif.com/gif-to-mp4) online tool by changing the gif to mp4.

![image](https://user-images.githubusercontent.com/70703371/232398690-f75e3b1a-dcfe-489a-9528-45e6e98ec888.png)


6. Saved the all the image.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/232398915-35741513-677f-4c49-a0f6-3045a02048c7.png)


7. Concate it and decode the base64.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/232399277-730c1583-a952-44b2-9c32-cd06c6976e9f.png)


8. Got the flag.

## FLAG

```
flag{g1f_or_j1f}
```
