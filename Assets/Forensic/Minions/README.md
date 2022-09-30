# Minions
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there:
https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg Can you help me? TIP: Decode the flag until you got a sentence.
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Download the file.
3. Strings the image.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193189919-accb6140-271e-4673-9a50-c8c4e760923a.png)

4. Go to the link.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193189954-d38c6266-eed3-4fed-8a3b-1f785f2dcc95.png)

5. Download the image.
6. Next, let's do **binwalk**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193270591-6679972c-9669-41a3-8b80-9c50bbd411b5.png)


7. Jump to the extracted folder.

![image](https://user-images.githubusercontent.com/70703371/193270627-fb8b920d-982c-4a90-a73d-e76b186199ec.png)


8. Extract the `.rar` file.

![image](https://user-images.githubusercontent.com/70703371/193274072-58339617-a4a0-4982-995e-87fbb36c61c9.png)


9. Combine the **strings** and **grep**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193274491-762e4aa9-3ee4-4cdc-988a-8cae60fb4e30.png)


10. Seems it's a base64 text, let's decode it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193275073-f1e9aab5-df15-43b8-8ccb-949f74aa0a8f.png)


11. Decode it again.

![image](https://user-images.githubusercontent.com/70703371/193275157-9e6b0641-fe8b-4247-88c3-39f831bccfc7.png)


12. Hmm.. They still gave us the base64 text.
13. Let's do it again.



10. Got the flag!


## FLAG

```

```


