# Accumulator
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I'll give you a flag if you can get a negative number by adding only positive numbers.

`nc rivit.dev 10009`

[FILE](https://ctflearn.com/challenge/download/1232)

## HINT: 
- NONE

## STEPS: 
1. First, download the file given.
2. Next, chech the file type.

> FILE TYPE

![image](https://user-images.githubusercontent.com/70703371/200119453-f57095c4-0e81-42f5-afb7-919820f5fa3a.png)

3. Not stripped means we can see the function's names.
4. Now check the file's protection.

> FILE PROTECTION

![image](https://user-images.githubusercontent.com/70703371/200119495-9eea49fe-0f09-4be6-bc6c-b2739ceab2bb.png)


5. Seems we can bufferoverflow the input.
6. Let's make the file executeable first by run `chmod +x task`, then run the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200119552-6b689cb2-8ed1-4a22-811b-f6a5410f8e3e.png)


7. Since it's related to bufferoverflow, try to
