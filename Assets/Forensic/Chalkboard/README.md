# Chalkboard
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/c27de35cbc60fdc349d7a292dcbbd0bab1ade615/Assets/Forensic/Chalkboard/math.jpg)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, let's combine **strings** and **grep**.
3. But we got nothing, now let's reduce the bytes when we strings it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193043873-3cdd1ab1-6bd5-4db1-8ce5-cb6411e95c8d.png)


4. Well i did simple **elimintation** and **substitution**, hence i got x -> 2 and y -> 5.
5. Got the flag!

## FLAG

```
CTFlearn{I_Like_Math_2_5}
```

