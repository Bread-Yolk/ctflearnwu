# Milk's Best Friend
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
There's nothing I love more than oreos, lions, and winning. https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y Have Fun :)
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Next, download the file.
3. Let's run **binwalk** and extract hidden files inside.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193405053-9152b574-946b-4cb6-a540-251cbf59a907.png)


4. Jump to the extracted folder.

![image](https://user-images.githubusercontent.com/70703371/193405069-7a635453-1758-4c4e-b8a5-3a508fa2a8c1.png)


5. Strings the `b.jpg`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193405115-9643fceb-136a-4fb2-996b-4815723c0aab.png)


6. Got the flag!

## FLAG

```
CTFlearn{eat_more_oreos}
```
