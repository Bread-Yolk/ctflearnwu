# Two times sixteen
> Write-up author: jon-brandy
## DESCRIPTION:
Your task is simple - call the function print_flag. It is guarded by a couple of ifs - good luck in defeating them.

nc rivit.dev 10000

## HINT:
- NONE
## STEPS:
1. After unzipping the file, we got 2 files -> binary and it's source code.
2. First, check the binary type and it's protections.

> 64 bit, not stripped

![image](https://user-images.githubusercontent.com/70703371/222120384-206e6d8a-e9f3-4f00-bbbd-0274e24899a4.png)


> VULN -> Partial RELRO, No Canary Found, No PIE

![image](https://user-images.githubusercontent.com/70703371/222120463-fff58f63-7b91-421c-b426-6be13eb20e0e.png)


3. No need to decompile the binary, because we have the source code, let's analyze it then.
4. 
