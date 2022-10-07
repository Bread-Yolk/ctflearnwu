# abandoned place
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
the flag is outside of the pic, try to find it. another hint: dimensions, dimensions, everything is in dimensions.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/76801c3cf531f742622496ad6cae5038f09b6d14/Assets/Forensic/abandoned%20place/abondoned_street_challenge2.jpg)

## HINT:
- NONE

## STEPS:
1. First, download the file.
2. Next, try to combine strings and grep to the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194572685-2bd94ead-859e-43ad-80a6-ff746a938c1c.png)


3. Found nothing.
4. Maybe we can find something if we reduce the bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194572798-e842b679-221b-48fa-b353-28a8c657b270.png)


5. Still nothing.
6. Then let's use **exiftool**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194572977-734fc1ea-e1ce-46ab-92bf-52c21cf8ec00.png)


7. Now let's run **eog**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194573381-9dcab5dd-8e2b-4c66-8185-94312c37bf38.png)


8. Even i used **stegsolve** but found nothing hidden using bit plane.
9. Maybe change the height or width of the image can give us any clue.
10. Open the image using **cyberchef** or using **hexedit**.
11. This time i used **hexedit**.
12. To change the height of JPG, we need to know this.

> NOTES

![image](https://user-images.githubusercontent.com/70703371/194574447-3e06ebff-3a66-4c4b-b9c7-0dd8f610a61c.png)


13. Now let's search `ff c0`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194575705-ef9c9432-835b-472e-ae68-c070ee2185e1.png)


14. We can conclude that these bytes are for the height.

![image](https://user-images.githubusercontent.com/70703371/194575924-c2980a8e-45b6-4c3b-a6ea-f66629399fe2.png)


15. Change the `03` to `07`, then run `eog` again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194576257-1400e76a-1e66-4c4d-9529-1dc38d43b23e.png)


16. Got the flag!


### FLAG

```
CTFlearn{urban_exploration}
```



## LEARNING REFERENCES:

```
https://blog.cyberhacktics.com/hiding-information-by-changing-an-images-height/
```
