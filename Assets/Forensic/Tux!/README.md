# Tux!
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/e885852e85a7de752e8a22ddccfa38d0275b9c39/Assets/Forensic/Tux!/Tux.jpg)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, let's see are there any hidden files inside.

![image](https://user-images.githubusercontent.com/70703371/193170917-dd266b9d-4196-408a-9691-9729c46e69a7.png)

3. Let's extract it using **foremost** , then jump to the `output` folder.

![image](https://user-images.githubusercontent.com/70703371/193171020-26470e23-c4f3-47d2-a5c1-d51d1330666e.png)


4. Go to the `zip` folder.

![image](https://user-images.githubusercontent.com/70703371/193171085-9c47e1a7-1dd0-4b9d-b262-6625f4ca6494.png)


5. Unzip it.

![image](https://user-images.githubusercontent.com/70703371/193171206-a8111da6-f115-47f9-88e7-572958be5ddd.png)


6. Seems we need to find the password.
7. Let's use exiftool to see are there any comments inside the image's file.

![image](https://user-images.githubusercontent.com/70703371/193171373-7a0b1a24-84f2-4966-acf6-7ccc903dff26.png)


8. I think it's a `base64` encoding, let's decode it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193171530-3cf22b2b-268c-4050-8340-7f6d6253c68b.png)


9. Got the pass, let's jump to the `zip` folder again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193171722-5b84ad8c-ff61-4726-8ab9-0f13027f7a5a.png)


10. 

