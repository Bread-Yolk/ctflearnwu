# Noise?
> Write-up author: jon-brandy
## DESCRIPTION:
Hey! I have intercepted this https://mega.nz/#!SPhCwATa!2i8_wI4t1j3VdnauXDB1OaW60l5hJAr3ylTxo_K9FeY from the Center for Interesting Arrangements. 
Out of all the documents the CIA holds, this seems to stand out because I don't see any "interesting arrangement" in this image. 
Pretty sure that this is just a bunch of noise... or is it? Look at this file closely and you'll (definitely) agree with me!
## HINT:
- NONE
## STEPS:
1. In this challenge we're given a .png file.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/da587c4b-c95f-4738-954c-6844cf2d23bb)

2. Running basic file checks shall resulting to none, until I ran `zsteg -a` found out that there's an embedded image data in red LSB.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/92a07872-f7b0-4066-bcfb-f7dbeb8a9bc2)


3. Let's extract it using stegsolve.

> RESULT


![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/a92582df-f0f8-4957-82aa-a7ae4a0da92b)


![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/6e8f7e61-c8d8-4d6d-aee6-93816d3571bc)



4. At glance nothing's different from the extracted png file other than the size of it. But running zsteg again to this image file resulting to another embedded image data.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/9511f2c7-b043-4392-903d-58a0e1a33c2e)


5. Interesting! Long stort short, I did the same thing over and over again and found the flag at the 14th time.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/40b3cac8-564a-41a8-90f5-38f29fd61af1)


## ALTERNATE SOLVES

1. You can use zsteg command --> `zsteg -E b8,r,lsb,xy noise.png > alt.png`.

## FLAG

```
flag{n0t_n0ise_4ft3r_4ll}
```
