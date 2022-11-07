# RSA Noob
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
These numbers were scratched out on a prison wall. Can you help me decode them? https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

## HINT:
- NONE

## STEPS:
1. First, open the link given.
2. Next, download the file.

> .TXT

![image](https://user-images.githubusercontent.com/70703371/200233085-444df0cf-06fa-4cf9-8526-287df4a224ef.png)


3. Based from the title and the strings we got, we can conclude it as RSA Cryptography.
4. Now let's get the 2 primes numbers by factoring the **N** value to [this](http://factordb.com/) online tools.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200233360-8f890364-300b-424c-b59c-426875254e37.png)


```
p = 416064700201658306196320137931
q = 590872612825179551336102196593
```

