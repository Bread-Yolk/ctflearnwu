# Up For A Little Challenge?
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0

You Know What To Do ...
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Next, download the `.jpg` file.
3. Then, let's combine strings with grep.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194704065-95e3931a-086f-4d69-9cc5-c218c0a9fd75.png)


4. Hmm.. let's strings it again but reduce the bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194704135-e78ab1ba-a035-4121-b5b1-51d72a02208b.png)


5. Let's open the link.

![image](https://user-images.githubusercontent.com/70703371/194704147-78267718-64fc-43f9-931f-567fc44cafe2.png)


6. A zip file, then the pass must be one of these two:

![image](https://user-images.githubusercontent.com/70703371/194705540-3c5094da-e34a-4cea-a83e-1c202689472c.png)


7. Download the zip file and let's try to unzip it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194704218-de8d88d3-b3ac-420d-a650-05a424bdf60b.png)


8. Surprisingly, we unzipped it without any pass or key.
9. Jump to this folder.

![image](https://user-images.githubusercontent.com/70703371/194704261-ee3f27ad-2de9-4c2a-b714-f1619c649968.png)


![image](https://user-images.githubusercontent.com/70703371/194704277-73dc6ccc-e4ec-48b9-8409-babfcdeee015.png)


10. Well i tried **stegsolve** and looks like it's not related to bit plane, also i combined **strings** and **grep** but got no clue.
11. But when i open the file in **hexedit**.
12. I found this clue.

![image](https://user-images.githubusercontent.com/70703371/194704801-cd5843cd-9420-4a36-b419-6fd67015767c.png)


13. Let's use **exif**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194705343-6e631e8d-8d78-41bc-83f7-dd93936b78bf.png)


![image](https://user-images.githubusercontent.com/70703371/194705362-90f8b138-9183-442e-968b-5d3d7fb21ace.png)


![image](https://user-images.githubusercontent.com/70703371/194705398-8b127927-6c48-4997-b8eb-b5d731c48919.png)


14. Got no clue.
15. Maybe let's see are there any hidden file or directory here.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194705420-fb3c0e93-8054-419f-ae4f-6624d2fa60b5.png)


16. Well there is one.
17. Check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194705427-b13d02be-e9e6-4138-bb5a-3ff2f0e250ae.png)


18. A zip file, let's unzip it then.

![image](https://user-images.githubusercontent.com/70703371/194705441-03b266a6-f2ed-4ceb-be46-64477273d737.png)


19. They ask the pass, let's input the pass we found before.
20. Sucessfully unzipped it using this pass:

> PASS

```
Nothing Is As It Seems
```

![image](https://user-images.githubusercontent.com/70703371/194705593-8e004b17-1ae7-4b63-a58e-5f41b76774a9.png)


![image](https://user-images.githubusercontent.com/70703371/194705603-5b722b63-fe56-4942-b79a-3d9d6b51708d.png)


21. Let's try to use **stegsolve** this time.

> FULL RED

![image](https://user-images.githubusercontent.com/70703371/194705759-61ec87cf-a7cc-467f-971e-b6103a56bc25.png)


22. Notice at the bottom right, there's a text.

> ZOOMED IN

![image](https://user-images.githubusercontent.com/70703371/194705777-6f5a3053-f753-45af-b8e1-2e6114869c9e.png)


23. Finally! We got the flag.

## FLAG

```
CTFlearn{hack_complete}
```
