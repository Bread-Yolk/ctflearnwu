# Domain name resolver
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Check IP of your favorite domain.

`nc rivit.dev 10004`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/219c3f872ee92e567d29e124b0c63dbaf5d44da4/Assets/Binex/Domain%20name%20resolver/task.tar.gz)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, unzip the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195493644-7c9f57c3-5e8c-495c-bda4-83ef9b200ab2.png)


3. Check the **file** type.

![image](https://user-images.githubusercontent.com/70703371/195493684-aa4d681e-dbfb-4f81-bedf-b9ff9e548f6e.png)


4. Great! It's not stripped, means we can see the functions names.
5. Check the file's protection.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195493789-8f18b3cc-d503-468f-bfc9-f639cd20696b.png)


6. Let's decompile the file.

> I USED GHIDRA




7. 
