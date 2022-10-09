# Digital Camouflage
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:

We need to gain access to some routers. 
Let's try and see if we can find the password in the captured network data: https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY 
Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
<br /> 
Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

Credit: picoCTF 2017

## HINTS:
- It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
- If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

## STEPS:
1. First, open the link given.
2. Next, download the `.pcap` file.
3. Let's open it in wireshark.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739050-77ec2cd5-9be3-4791-8acb-328aef474234.png)


4. Found this quite interesting.

![image](https://user-images.githubusercontent.com/70703371/194739291-46322283-49b0-4fef-9ab4-46575f8dc180.png)


5. Let's fiter the packets by type this at the filter bar -> `ip.addr == 10.0.0.1`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739315-b98f6e34-9c05-4b7d-b0af-9397a5b53a57.png)


6. Follow the http stream for this one.

![image](https://user-images.githubusercontent.com/70703371/194739333-149f3d74-f759-49ff-8ac6-8c41ce30c4a5.png)


![image](https://user-images.githubusercontent.com/70703371/194739342-a45fb413-44ad-4989-84e8-4a011fd57aa5.png)


7. Still got no clue anyway, since there are **GET** method, maybe there are few **POST** method too.
8. Let's filter it then -> `http.request.method == POST`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739391-db358029-d26c-4fac-8642-745a2837c6f9.png)


9. We got one here and it's an URLENCODED message.
10. Follow the http stream.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739410-861e2999-4944-49d2-afd1-784a85a1ab2b.png)


11. We got clues here.
12. The username & the pass, but since the pass is urlencoded.

> THE PASS

```
UEFwZHNqUlRhZQ%3D%3D
```

13. I decoded it using [this](https://www.urldecoder.org/) online tools.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739444-cdb4af13-a1df-4d58-843e-35558493462f.png)


```
UEFwZHNqUlRhZQ==
```

14. It's a base64 text, decode it to plain text.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/194739470-4c90866c-1a43-4bbf-9b08-10c5fa72f5e5.png)


15. Hmm.. Got weird result. But based from the hint given, this must be the correct flag!
16. Turns out it is! We got the flag.


## FLAG

```
PApdsjRTae
```
