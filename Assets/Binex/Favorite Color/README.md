# Favorite Color
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
What's your favorite color? Would you like to share with me? Run the command: `ssh color@104.131.79.111 -p 1001` (pw: guest) to tell me!
## HINT:
- NONE
## STEPS:
1. First, paste the **ssh** command at your linux terminal.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744746-859d42e7-810b-48c2-9f83-8864a49c4aec.png)


2. Based from the description, enter the pass as **guest**.
3. And we are logged in.

![image](https://user-images.githubusercontent.com/70703371/194744762-0b239ac9-342c-40e7-afe5-e4d741875a51.png)


4. Looks like we have 4 files.

![image](https://user-images.githubusercontent.com/70703371/194744769-ba36a56c-b3d8-4654-a05d-fd5631ad4b35.png)


5. Let's check are there any hidden files inside this directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744792-50d4a124-9b42-4916-a44a-cd48ce87102f.png)


6. Well, there are. But looks like it's not useful.
7. Anyway, let's run the **color** program.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744846-a76cea10-149c-4bad-9de3-330e4f549640.png)


![image](https://user-images.githubusercontent.com/70703371/194744854-dbf9075b-7b21-4668-9e29-46bac06f6c9c.png)


8. Hmm.. what may happen if we enter 100 A's.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194744902-cc1268e9-efee-46ce-a303-4c1db424fd88.png)


9. Got segmentation fault.
10. Let's run the program in gdb and enter 100 A's as the input.

> GDB

![image](https://user-images.githubusercontent.com/70703371/194744959-c21264be-8c25-40a7-8a2e-cbba43464ad4.png)


11. We got clue here, we can control the return address.
12. We need to know how many padding should we add, so we can overwrite the eip.
13. 


