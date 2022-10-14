# Don't Bump Your Head(er)
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Try to bypass my security measure on this site! http://165.227.106.113/header.php
## HINT:
- NONE
## STEPS:
1. First, open the link given.

![image](https://user-images.githubusercontent.com/70703371/195791373-7030a4c9-3a52-4795-ba65-ebcdd2bbb324.png)


2. Let's open the website using **burpsuite**, set the **intercept** to on and click action -> send to repeater -> click the send button.

> ![image](https://user-images.githubusercontent.com/70703371/195792229-b5ce8099-8ae1-47a5-8909-d250cdb046bf.png)


3. Change the `User-Agent` value to `Sup3rS3cr3tAg3nt`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195792494-a1113302-ed9c-4dc7-a956-7e5c0bf275a2.png)


4. Now add the `Referer` and set the value as `awesomesauce.com`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195794566-cfdb39e2-0d29-43ce-8a96-995fdae2d273.png)


![image](https://user-images.githubusercontent.com/70703371/195794957-9fafae63-f867-4e32-b763-2c572faaa106.png)


5. It seems, my burpsuite is broken. 
6. Let's use **curl**.

> COMMAND

```sh
curl -A Sup3rS3cr3tAg3nt --referer awesomesauce.com http://165.227.106.113/header.php
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195795612-cd973473-6d48-4e86-97ad-523ed4a787aa.png)


7. Got the flag!

## FLAG

```
flag{did_this_m3ss_with_y0ur_h34d}
```
