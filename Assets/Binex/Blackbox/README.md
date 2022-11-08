# Blackbox
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
What is 1 + 1? Run the command: ssh blackbox@104.131.79.111 -p 1001 (pw: guest).
## HINT:
- NONE
## STEPS:
1. First, runt the command given and enter the password as `guest`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200485537-5ab862d8-604d-4d6f-96a3-470da6d161a5.png)



2. Let's see what's inside.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200485590-f7de95bc-297e-4389-8613-98de27ca880e.png)



3. Check the `blackbox` file type.

![image](https://user-images.githubusercontent.com/70703371/200485666-2e2a199a-6ce5-4819-b397-23bacd93de91.png)



4. Check the file's protection.

![image](https://user-images.githubusercontent.com/70703371/200485833-d7dd9fa1-5569-4e80-86cd-8748652b3db5.png)



5. Seems we can't check it, however let's run the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200485926-062c0d09-bb27-4265-b433-e90ce22b2c66.png)



![image](https://user-images.githubusercontent.com/70703371/200485985-26d7f1a0-ef33-49f3-bb76-54aa19cea9c0.png)



6. Hmm.. maybe we can try to overflow it.

> START WITH 74 CHARACTERS.

![image](https://user-images.githubusercontent.com/70703371/200486974-1db91db0-1348-4a6a-92ea-c29ded77e2f6.png)



7. How about we input characters (?), because we suggest they use `gets()` to get input.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200490212-bbb69926-f305-491a-98a0-797e7165d533.png)



8. Yes, exactly.
9. Now, let's try to add 78 characters.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200490605-6fc88aa1-91c6-47db-8e88-b72a37577e12.png)



10. Now add another 4 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200490766-22c51132-c49c-4fda-b3ca-24f7490c90c6.png)



11. We got different output now.
12. Maybe add another 4 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200490928-0254f9ec-8bbd-487e-a891-dc9f2c659c4a.png)



13. Hmm, add another 4 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200491118-d6541b21-59bd-42d2-8544-3d82bfcf0424.png)



14. The program crashed.
15. As we know, we got the first different value when we add the padding as 82 bytes.
16. Let's reduce it to 81.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200491914-19b0ed3d-019a-4334-9eab-402179ae8331.png)



17. Reduce it again to 80.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200491996-b179e320-9fc2-412f-80a1-36514f1a7a66.png)



18. Finally! We got the flag.

## FLAG

```
flag{0n3_4lus_1_1s_Tw0_dumm13!!}
```






