# Blackbox
#### Write-up author: [jon-brandy]()
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


> GO TO 78

![image](https://user-images.githubusercontent.com/70703371/200487063-89550ee0-4125-4813-ae13-89113aeaecac.png)


> NOW GO TO 82

![image](https://user-images.githubusercontent.com/70703371/200487252-d8498b81-255f-4c82-929e-809355897768.png)


7. We got different output now.
8. Let's keep going.

> 86 CHARACTERS

![image](https://user-images.githubusercontent.com/70703371/200487443-b54679fc-000b-4fb6-9039-2ae305174e40.png)


> 90 CHARACTERS

![image](https://user-images.githubusercontent.com/70703371/200487615-e20d687b-1ae0-495b-8aff-65262bd8bcc4.png)


9. Great we found the bufferoverflow here.
10. Now concate the 2 hex with little endian form as the postfix.

![image](https://user-images.githubusercontent.com/70703371/200488161-66d8cc39-0312-4a96-a5d0-4007d7d99364.png)


11. Hmm.. maybe we have to change the padding bytes as `1` (?)
12. But we need to find the exact overflow padding first, let;s try to add 84 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200488610-31d12cd0-309e-474b-80eb-b46323e32dc4.png)


13. How about another 4 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200488709-a05d8eff-ef5f-43a3-8cb3-b4d492ebd3d3.png)


14. Value not changed, but maybe let's drop it to 80 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200488785-2e2462b5-968f-4c7e-9f34-4de7121c3af2.png)


15. I'm guessing 84 bytes is the correct padding.
16. Now concate the 2 decimal value in hex as the postfix.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200489209-65772b70-ef60-4ed2-ba38-059a50cd73cb.png)






