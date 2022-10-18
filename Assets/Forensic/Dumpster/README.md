# Dumpster
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I found a flag, but it was encrypted! Our systems have detected that someone has successfully decrypted this flag, 
and we stealthily took a heap dump of the program (in Java). Can you recover the flag for me? 
Here's the source code of the Java program and the heap dump: https://mega.nz/#!rHYGlAQT!48DlH2pSZg10Ei3f-Ivm7RoNBbV16Qw0wN4cWxANUwY
## HINT:
- NONE
## STEPS:
1. First, open the link given.
2. Next, download the file given.
3. Unzip the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196395795-1498fe3a-0b11-4a2c-b659-44526a700b0d.png)


4. Let's run the `java` program.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196396460-afbeb92e-11ea-4f0a-932f-cf98bb986897.png)

> THE SOURCE CODE

```java
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Decryptor
{
	public static final String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";
	private static class Password
	{
		private byte[] passHash;

		public Password(char[] pass) throws Exception
		{
			MessageDigest digest = MessageDigest.getInstance("SHA-256");
			this.passHash = Arrays.copyOf(digest.digest(new String(pass).getBytes("UTF-8")), 16);
		}
		
		public byte[] encrypt(byte[] msg) throws Exception
		{
			SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
			Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
			cipher.init(Cipher.ENCRYPT_MODE, spec);
			return cipher.doFinal(msg);
		}
		
		public byte[] decrypt(byte[] msg) throws Exception
		{
			SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
			Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
			cipher.init(Cipher.DECRYPT_MODE, spec);
			return cipher.doFinal(msg);
		}
	}
	
	public static void main(String[] args) throws Exception
	{
		Password pass = new Password(System.console().readPassword("Enter password to decrypt flag: "));
		System.out.println(new String(pass.decrypt(Base64.getDecoder().decode(FLAG.getBytes()))));
		Thread.sleep(5000); //We did a heap dump right here.
	}
}
```

5. It seems we need to find then password first.
6. Let's open the other file using `visualvm`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196397551-9e025a2f-1fc9-4ab0-896e-8e6071f90e52.png)


7. Choose `threads`.

![image](https://user-images.githubusercontent.com/70703371/196397720-bbc49ea1-fd22-4372-b1ff-e221c81d4a57.png)


> RESULT

![image](https://user-images.githubusercontent.com/70703371/196397790-43b56dda-102b-4dbc-80a5-be980bf29fcf.png)


8. Scroll to the bottom.
9. Open the main.

![image](https://user-images.githubusercontent.com/70703371/196397998-0c3f9714-1fd0-4680-9d7b-a4131fe37562.png)


10. Open the **local variable decryptor**.

![image](https://user-images.githubusercontent.com/70703371/196398187-70286e11-992e-4c94-9f93-ad3d0c976c7a.png)


11. Open `fields -> pass hash`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/196398344-07e0814b-fae2-4411-b095-6a2f87ba772e.png)


12. Now 
