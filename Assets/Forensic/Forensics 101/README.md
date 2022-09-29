# Forensics 101
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Think the flag is somewhere in there. Would you help me find it? https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c
## HINT:
- NONE
## STEPS:
1. Click the given link.
2. Download the `.jpg` file.

> JPG

![95f6edfb66ef42d774a5a34581f19052](https://user-images.githubusercontent.com/70703371/192997125-23fc4002-f1eb-4a5c-a62d-c07d62b8585a.jpg)


6. Now let's extract what's inside using binwalk.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193006368-3968511d-93c3-4f18-8503-d6e9dbb6f719.png)


7. We got nothing.
8. Maybe we can start from the basic again by combine **strings** and **grep**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193006539-dbe45a97-c991-4f97-a0c6-9496869f050c.png)

9. Hmm.. Kinda confused, i tried to change the keyword to `flag`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193006690-eccf5911-bf00-4226-abb9-02c5a5b4b5bf.png)

10. Finally, we got the flag!

## FLAG

```
CTFlearn{wow!_data_is_cool}
```





