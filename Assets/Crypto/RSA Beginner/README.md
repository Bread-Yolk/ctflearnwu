# RSA Beginner
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I found this scribbled on a piece of paper. Can you make sense of it? https://mega.nz/#!zD4wDYiC!iLB3pMJElgWZy6Bv97FF8SJz1KEk9lWsgBSw62mtxQg
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Next, download the file.

![image](https://user-images.githubusercontent.com/70703371/200238404-49548bda-0b50-4b7e-8296-3a4f91bb5716.png)


3. Looks like it's just simple RSA.
4. For this solution i made this python script:

```py
import os

os.system('clear')

n = 245841236512478852752909734912575581815967630033049838269083
e = 3
c = 219878849218803628752496734037301843801487889344508611639028
p = 416064700201658306196320137931
q = 590872612825179551336102196593

d = pow(e, -1, (p-1)*(q-1))
decrypt = hex(pow(c,d,n))
decrypt = decrypt.strip("0x")
result = bytearray.fromhex(decrypt)
print(result.decode())

```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/200238857-12e592d8-d719-4e38-8a3f-dedf5af8aac3.png)


5. Got the flag!

## FLAG

```
abctf{rs4_is_aw3s0m3}
```
