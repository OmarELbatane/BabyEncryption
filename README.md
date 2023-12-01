# BabyEncryption
Hello there! This CTF is a crypto challenge that I found on Hack The Box, and I said, "Why not give it a go?" (it looked interesting).

After downloading the directory and entering the password, I had 2 files. The first was this Python code with the encryption function in it:

![Image Description](/ctf0.png)

And the second one was this text message:

![Image Description](/ctf1.png)

So, I assumed that this text was the encrypted message used by the function above.
First of all, I needed to understand what the Python code does, so I could decrypt the message for the flag.

![Image Description](/ctf3.png)

In the beginning, the code:

- Takes a message (in this case, our flag).
- Then, it creates an empty list.
- For every character in the message, it takes that character and applies the formula to cipher the message.
- Then, it puts that character in the list, as a hex.

Example:

![Image Description](/ctf4.png)

Will give us this:

![Image Description](/ctf5.png)

Now that I know how the code works, let's start by finding the reverse formula to decrypt the message.

<h2> Formula </h2>
Let's suppose 'e' represents the encrypted character and 'd' is the decrypted text, which means we have:

- e = 123 * d + 18 mod 256
- Which means that 123 * d + 18 = e mod 256
- 123 * d = e -18 mod 256, and since -18 = 238 mod 256
- 123 * d = e + 238 mod 256
- Now, I need to find the inverse of 123 so that when I multiply 123 by this inverse, I'll have 123 * inv = 1 mod 256
- With some calculations, we find that 256 * 37 - 77 * 123 = 1
- Which means that -77 * 123 = 1 mod 256 -> 123 * 179 = 1 mod 256 (since 179 = -77 mod 256)
- So, we find that d = (e + 238) * 179 mod 256

![Image Description](/ctf6.png)

<h2> Code </h2>

Now that I can decrypt the code, I just need to create a program that will reverse the calculations.

The first problem that I found was that I needed to start from the last element (I realized after finishing the CTF that there was a more optimal function).
So, I started by listing the elements from the last one to the first:

![Image Description](/ctf7.png)

What you should know is that the text was encrypted in hexadecimal, with two characters. 
For example, 156 in decimal is 16 * 9 + 12, which means 9C in hexadecimal. 
So, I needed to take 2 elements every time (e.g., 9C) and convert it into an integer. This is what I came up with:

![Image Description](/ctf8.png)

I take two characters every time, convert them into an integer, then cast them into a character and append them to the list.

![Image Description](/ctf9.png)

At the end, I added this line of code to reverse the message and output it as a string. This is what I got when I used the text message in the code:

![Image Description](/ctfresultat.png)

So, after getting the flag, all I had to do was submit it on Hack The Box.

![Image Description](/ctffinal.png)
