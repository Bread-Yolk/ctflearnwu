# A CAPture of a Flag
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark. 
https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4

## HINT:
- NONE.
## STEPS:
1. First, open the link given.
2. Next, download the file.
3. Check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193405251-b2d7465c-314f-4a51-9bb5-e4c767f7a806.png)


4. Let's open the file using **wireshark**.

> WIRESHARK

![image](https://user-images.githubusercontent.com/70703371/193405344-7842b9a0-ff20-4a2c-99ee-8ad86e40d032.png)


5. Let's filter the stream with `HTTP` protocol only.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193405788-950be31d-bd96-4584-bd3d-8c1e72357e7d.png)


6. Something caught my attention, there's a base64 text.

![image](https://user-images.githubusercontent.com/70703371/193405842-01d035dd-4273-4d26-8fb3-51d686348349.png)


7. Anyway let's filter the stream showed with only HTTP protocol with GET as the header.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193405918-a23b481f-ea94-4810-87cc-9d285e160327.png)


8. Hmm.. let's try the one we found at first.
9. Follow the HTTP Stream then decode the base64 text.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193405943-8e17ecbc-859b-4368-a5a9-3be12c2d6884.png)


![image](https://user-images.githubusercontent.com/70703371/193405954-31d1c849-1097-4941-aafd-9f78e8fbe97c.png)


10. Got the flag!


## FLAG

```
CTFlearn{AFlagInPCAP}
```
