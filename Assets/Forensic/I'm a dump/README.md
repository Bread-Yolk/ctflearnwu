# I'm a dump
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. The flag is in the format CTFlearn{*}

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/a42a2a35c6f7036566f33ed0d4acab92b47b7d44/Assets/Forensic/I'm%20a%20dump/file)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193034897-d8dbd5ae-8633-4a49-b90a-c57a571ece82.png)

3. Since it's an executable file, let's make it executeable by run **chmod**.
4. Then run the file.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/193035059-4f4d65f4-e7f8-411a-9df2-8225a54e58d6.png)


5. Surprisingly, we got nothing.
6. Let's strings it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193035406-61b13242-dba6-4bf5-ada0-b35153de94e2.png)


7. I think there's a flag.

![image](https://user-images.githubusercontent.com/70703371/193035511-59f6f61f-f184-447b-b52e-2b743ab67f71.png)

8. Remove the H characters.
9. We got the flag!

## FLAG

```
CTFlearn{fl4ggyfl4g}
```
