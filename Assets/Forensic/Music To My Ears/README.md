# Music To My Ears
> Write-up author: jon-brandy
## DESCRIPTION:
This audio file is supposed to say the flag, but it's corrupted! ): <br> https://mega.nz/#!jexRzTzD!Fd3tD8ZcLquXJrsycMFUzozC9MHqaG-srUBfGREtL-0 <br /> <br />Can you fix it and input the flag? <br>
## HINT:
- NONE
## STEPS:
1. In this challenge we're given a corrupted `.m4a` file.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/81eb961f-dbb0-4f01-afe6-ea47df73663d)


2. Actually I solved it unintended I guess, because I used online web-tools --> `https://www.onlineconverter.com/convert/34b845da9970540ef34d37c1bcd3cad1aa`.
3. Simply upload the file, hence you shall got the uncorrupted audio.
4. The intended way should be using `FAAC` and `FAAD`.

> ABOUT FAAD AND FAAC

```
https://sysfrontier.com/en/2014/12/31/hello-world/
```

5. Anyway, simply listen to the audio, it shall dictate all the letter of the flag.

## FLAG

```
1_c4n_f1x_it
```
