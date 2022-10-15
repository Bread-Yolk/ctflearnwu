# Naughty Cat 
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I think my cat is hiding something...

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/173508aca7d12bf2c576d8ed2f97495f0bd5788f/Assets/Forensic/Naughty%20Cat/cut3_c4t.png)

## HINT:
- NONE
## STEPS:
1. First, download the given file.
2. Next, let's extract any hidden files inside with **binwalk**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195973866-7e64223b-7166-41d0-9fb8-0630c3091853.png)


3. Open the `mp3` file using **audacity**.

> RESULT - CTRL + SCROLL to adjust the audio strecth

![image](https://user-images.githubusercontent.com/70703371/195974022-5cbf482c-d2e2-4996-8179-a729fc78d313.png)


![image](https://user-images.githubusercontent.com/70703371/195974142-d1d066a6-1de7-4cb6-86a9-f55890774869.png)


4. But when i submitted it, it said the flag is incorrect.
5. Let's try to extract this `.rar` file.

![image](https://user-images.githubusercontent.com/70703371/195974445-dc419d72-aae5-4410-a1e5-a71c403fba27.png)


6. But it seems we got problem here.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195974455-f86d1827-3d86-4395-b2e6-46059727e656.png)


7. Weird.
8. Let's check the file with **hexeditor**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195974486-fcf730fd-6703-40a0-ab40-dea4646aac50.png)


8. Turns out it's corrupted, we need to change the `Cat!` to `Rar` by change the hex value from -> 43 to -> 52 and from 74 to 72

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195974547-9903cdb4-ca69-4259-9dbb-a61861db83f6.png)


9. Try to unrar it again!

![image](https://user-images.githubusercontent.com/70703371/195974571-690d732a-2f60-4a52-aa79-3afee8879117.png)


10. Input the pass as -> `sp3ctrum_1s_y0ur_fr13nd`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195974586-0e0e5bec-a23d-43a8-8e26-07031bb80720.png)

11. Strings the extracted `.txt` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195974603-91150d17-0eba-4bb8-8710-8b9f7aaf68db.png)


12. Decode the **base64** text.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195974630-1f76d876-45ed-4961-825f-a5e1dc8e32ab.png)


13. Got the flag!

## FLAG

```
f0r3n51cs_ma5t3r
```



