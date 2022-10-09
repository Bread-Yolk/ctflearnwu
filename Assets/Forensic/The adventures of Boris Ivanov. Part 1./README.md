# The adventures of Boris Ivanov. Part 1. 
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The KGB agent Boris Ivanov got information about an attempt to sell classified data. 
He quickly reacted and intercepted the correspondence. Help Boris understand what exactly they were trying to sell. 
Here is the interception data: https://mega.nz/#!HfAHmKQb!zg6EPqfwes1bBDCjx7-ZFR_0O0-GtGg2Mrn56l5LCkE
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Next, download the `.jpg` file.
3. Let's strings the image but reduce the bytes length.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194752986-ab5f8220-92ad-453c-bd3a-d81588b23d74.png)


4. We got clue here -> GIMP.
5. So i think we can use **stegsolve** for this challenge.
6. Open stegsolve, then choose `analyze` -> `stereogram solver`.
7. Moved to offset **102**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194754342-5a6e8f94-a956-41b7-b109-45248089d6fc.png)


8. Got the flag!

## FLAG

```
flag{d0nt_m3s5_w1th_th3_KGB}
```
