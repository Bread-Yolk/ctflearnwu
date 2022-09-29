# Taking LS
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Just take the Ls. Check out this zip file and I be the flag will remain hidden. https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

## HINT:
- NONE

## STEPS:
1. First, open the link given.
2. Download the `.zip` file.
3. Unzip the file.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/193008366-0af5f868-8efe-476f-82d8-6f816edce4ef.png)

4. Let's go the `'The Flag'` directory first.

![image](https://user-images.githubusercontent.com/70703371/193009501-70f1bdae-ed00-4ed7-a2cf-dbdf1a018a7f.png)

5. Hm.. Kinda sus, let's run `ls -a` to list all hidden directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193009603-26248f4b-8b55-48f6-8b47-0b18560710d8.png)

6. We found the `.ThePassword` directory, means the pdf must be locked.
7. Let's jump there.

![image](https://user-images.githubusercontent.com/70703371/193009764-0b9943c9-0f83-4838-9a08-fe28266ae49e.png)

8. Strings it.

![image](https://user-images.githubusercontent.com/70703371/193009832-038dadd4-7d0a-4b31-8c57-77d15f8605ca.png)

9. Great! Let's open the pdf and input the pass as -> `Im The Flag`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193010197-51dbe680-1dda-40ff-b260-2e3756b316d3.png)

10. Finally, we got the flag!

## FLAG

```
ABCTF{T3Rm1n4l_is_C00l}
```

