# Simple Steganography
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/430ef111d31de2f3facf3639378146375a49644f/Assets/Forensic/Simple%20Steganography/Minions1.jpeg)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Based, from the description, we could use **steghide** to solve this challenge.

> STEGHIDE

![image](https://user-images.githubusercontent.com/70703371/193182381-5af88e64-cda8-4fb4-ac1c-c70fbd4bc661.png)


3. Seems we need to find the pass.
4. Let's use exiftool to see are there any hidden comments or any usefull hints.

> EXIFTOOL

![image](https://user-images.githubusercontent.com/70703371/193182824-f23b9282-fee7-4961-a21f-5ef6d7d51982.png)


5. I think this might be the pass.


![image](https://user-images.githubusercontent.com/70703371/193182902-a5238353-c848-491c-952b-ebc87e3480ec.png)


6. Let's input the pass as `myadmin`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193182991-d88aa300-e68f-40e8-8a2b-daf7e2bf150e.png)


7. Strings it.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/193183279-f128b376-a8c8-4a8f-870b-9881f5f90ff1.png)


8. It is known that it is a base64 encoding text, so let's just decode it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193183552-beccbb90-7874-42b6-b0fa-ddc9d7d0eaad.png)


9. Finally, we got the flag.

## FLAG

```
CTFlearn{this_is_fun}
```
