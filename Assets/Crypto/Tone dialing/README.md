# Tone dialing
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
At 1pm I called my uncle who was 64 years old 10 months ago, but I heard only that. Later I started thinking about the 24 hour clock.

I hope you will help me solve this problem

[FILE](https://ctflearn.com/challenge/download/889)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Since i'm new to cryptography, so i did small outsource about it.

![image](https://user-images.githubusercontent.com/70703371/200157910-b86378eb-bb15-47b7-af46-b5633fd388ba.png)


3. Seems we need to use a tools called **dtmf**. Since i don't have it on my kali linux, so i used [this](http://dialabc.com/sound/detect/index.html) online decoder.

> DOCUMENTATION

```
https://github.com/ribt/dtmf-decoder
```

![image](https://user-images.githubusercontent.com/70703371/200162448-d719817c-9492-49bf-9192-6e4b1ac7e5af.png)


![image](https://user-images.githubusercontent.com/70703371/200162464-e19fbf93-4212-41d0-a3e8-b40caa0b16cd.png)


4. Concate all the decimal value we got.

> RESULT

```
67847010810197110123678289808479718265807289125
Listen the audio and seperate the num based on the "beep", got this ->  67 84 70 108 101 97 110 123 67 82 89 80 84 79 71 82 65 80 72 89 125
```

5. Convert it to char.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/200163176-ae0f4f1e-77db-4843-a1fb-25c54f304b36.png)


6. Got the flag!


## FLAG

```
CTFlean{CRYPTOGRAPHY}
```



