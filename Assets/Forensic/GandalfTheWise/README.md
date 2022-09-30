# GandalfTheWise
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/193060899bc1cf8d4ff839bc8f33929fdc106b0c/Assets/Forensic/GandalfTheWise/Gandalf.jpg)

## HINT:
- NONE
## STEPS:
1. First, download the file first.
2. Next, use exiftool to see are there any hidden comments or clues.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193185035-b2b09f1e-56bf-43e6-a55d-0acd7363ce6e.png)


3. The comment value seems like a base64 text.
4. Decode it.

![image](https://user-images.githubusercontent.com/70703371/193185119-b04fede4-8801-490e-973f-1c95a10a8343.png)


5. Turns out it's an incorrect flag.
6. Hmm..
7. 
