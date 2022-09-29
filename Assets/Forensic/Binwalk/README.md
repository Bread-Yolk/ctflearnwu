# Binwalk
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Here is a file with another file hidden inside it. Can you extract it? https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Next, download the image.
3. Based from the title, we may use `binwalk` to see files inside the image and extract it using the `-e` command.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193011970-dfaa036f-e4c4-4cf2-ab83-dc39ab5a8ee9.png)

4. Jump to the new folder we got.

![image](https://user-images.githubusercontent.com/70703371/193012165-cfa1f00d-7d6b-4fdc-961b-a376044914f5.png)


5. Before we extract it check what's inside first.

![image](https://user-images.githubusercontent.com/70703371/193013090-067bf73f-d54d-4ac4-91ff-9d38c6aff933.png)

6. Since it has a `.png` file, let's use **foremost** to extract it.

![image](https://user-images.githubusercontent.com/70703371/193013220-99beb677-14a5-4d22-ad2a-84a690d89f55.png)


7. Jump to the `cd` folder.

![image](https://user-images.githubusercontent.com/70703371/193013346-95092523-61ce-437d-bd1f-4f8521291d38.png)

8. Jump to the `png` folder.

![image](https://user-images.githubusercontent.com/70703371/193013418-7c2368da-8e57-473f-9af0-105499536d49.png)


9. Run **eog** to see the image.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/193013539-0b12980b-c581-4f02-8b53-653ddd48b9aa.png)


10. Finally, we got the flag!

## FLAG

```
ABCTF{b1nw4lk_is_us3ful}
```
