# POST Practice
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? 
http://165.227.106.113/post.php
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Let's open the website using **burpsuite**.
3. Set the intercept to **on**.
3. Click `open browser`.
4. Paste the link there and press forward at the **burpsuite**.
5. Next, refresh the page again, then click **action** then `send to repeater`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195620204-7f7f43cc-abad-4ed0-91a4-b8ff7d0a6d2a.png)


6. At the `repeater`, click the `send` button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/195620396-a93925f5-2f1e-43d2-9070-03fd3d17656a.png)


7. Notice there's a comment at the `response` page.

![image](https://user-images.githubusercontent.com/70703371/195620500-736b6fdf-0118-4a52-8a14-525354512035.png)


8. Let's use `curl`


