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

5. Next we need to find the private key in order to decrypt the ciphertext.

> THE FORMULA FOR DECRYPTION

![image](https://user-images.githubusercontent.com/70703371/200233997-f81a2582-6a61-49a6-988b-618640d29dc0.png)


6. So for this solution, i made this python script.

> THE SCRIPT

```py
import os

os.system('clear')

n = 245841236512478852752909734912575581815967630033049838269083
e = 1
c = 9327565722767258308650643213344542404592011161659991421
p = 416064700201658306196320137931
q = 590872612825179551336102196593

d = pow(e, -1, (p-1)*(q-1))
decrypt = hex(pow(c,d,n))
decrypt = decrypt.strip("0x")
result = bytearray.fromhex(decrypt)
print(result.decode())

```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/200234962-5f828d89-6e96-41ea-a029-09c14b105052.png)


7. Got the flag!

## FLAG

```
abctf{b3tter_up_y0ur_e}
```
