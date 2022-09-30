# PDF by fdpumyp
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Hi, just as we talked during a break, you have this file here and check if something is wrong with it. 
That's the only thing we found strange with this suspect, I hope there will be a password for his external drive

Bye

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/b2d8f0a090eca853c464adfcd7f948a2a649fe87/Assets/Forensic/PDF%20by%20fdpumyp/dontopen.pdf)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. As usual, strings it first.

![image](https://user-images.githubusercontent.com/70703371/193184268-b3a75f62-c871-4a3b-81e9-297c3ee807f0.png)


3. We got few clues there, under the `secret data`.
4. Obviously it is a base64 encoding text.

![image](https://user-images.githubusercontent.com/70703371/193184505-6eb2ac4d-ee07-4e3b-a794-00371ddf5c21.png)


5. Let's decode it straightaway.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193184539-08b227dc-75fb-45ec-ae6c-e12cb1d6d0eb.png)


6. Got the flag!

```
CTFlearn{)_1l0w3y0Um00my123}
```

