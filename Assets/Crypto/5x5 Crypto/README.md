# 5x5 Crypto
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Ever heard of the 5x5 secret message system? If not, basically it's a 5x5 grid with all letters of the alphabet in order, 
without k because c is represented to make the k sound only. Google it if you need to. A letter is identified by Row-Column.
All values are in caps. Try: 1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}

## HINT:
- NONE

## STEPS:
1. Based from the title, we can conclude , that it's **Polybius Square Cipher**. 
2. Got the clue here.

![image](https://user-images.githubusercontent.com/70703371/200236751-a6532593-a6b9-424e-8381-4a0c4ef5ccb2.png)


3. Means the table will look like this:

![image](https://user-images.githubusercontent.com/70703371/200236969-abdd332c-ff35-422d-a2e6-7c6b97cb76b5.png)


4. Since i can't make the script, let's find the value 1 by 1.

> EXAMPLE

```
1-3 -> row 1, column 1 -> C
4-4 -> row 4, column 4 -> T
2-1 -> row 2, column 1 -> F

ETC.
```

> FINAL RESULT

```
CTF{THUMBS_UP}
```

5. Got the flag!

## FLAG

```
CTF{THUMBS_UP}
```
