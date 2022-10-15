# Exclusive Santa
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Dear Santa,

Hey! There are so many toys that I want, but I just don't have the money. I don't care which toy I get as long as it's one or the other, but not both!
- CTFlearn

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/83367181fecf463938caee85b7697b058b91ab20/Assets/Forensic/Exclusive%20Santa/Exclusive_Santa.rar)

## HINT:
- NONE

## STEPS:
1. First, download the file given.
2. Next, unrar the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195973134-272b1c70-fb20-4923-a4e3-378266f9aeeb.png)


3. Let's see both images.

> 1.PNG

![image](https://user-images.githubusercontent.com/70703371/195973172-b5e991ec-b20b-4ddb-90dc-e042026e7de9.png)


> 3.PNG

![image](https://user-images.githubusercontent.com/70703371/195973162-e46ebe25-8571-4d88-b190-a07dbb581329.png)


4. The `3.png` caught my attention, i think this might be a clue.
5. We need to find other image so we can combine it using **stegsolve**.
6. Run **foremost** for `1.png`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195973560-e17877ff-6eda-4022-9f0e-66e3f32c2543.png)


7. Got nothing, run **foremost** for `3.png`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195973428-4705fe3c-a528-4fef-93a0-895bdedf3437.png)


![image](https://user-images.githubusercontent.com/70703371/195973434-a9c957c4-0952-4a30-a524-fe694e9d2271.png)


8. Hmm.. Let's combine it with `1.png` using **stegsolve**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195973495-faf0f118-1f11-41ff-88e8-b105e9a7a725.png)


9. Got the flag!

## FLAG

```
CTFlearn{Santa_1s_C0ming}
```
