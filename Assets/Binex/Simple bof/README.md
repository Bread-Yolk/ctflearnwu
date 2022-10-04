# Simple bof
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Want to learn the hacker's secret? Try to smash this buffer!

You need guidance? Look no further than to Mr. Liveoverflow. He puts out nice videos you should look if you haven't already

`nc thekidofarcrania.com 35235`

[FILE](https://github.com/Bread-Yolk/ctflearnwu/blob/defef2a071ebf4736bf939098b307008378d6b8b/Assets/Binex/Simple%20bof/bof.c)

## HINT:
- NONE
## STEPS:
1. First, download the `.c` file given.
2. Next, let's run the netcat first.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193816845-173c0654-c109-4d73-951c-46593ceb105d.png)


3. Looks like it just a simple bufferoverflow.
4. Let's input any length of A's.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/193816971-cc951b12-bec6-4250-b368-8920ab600b48.png)


5. It said we overflowed too much.

