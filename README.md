# BabyEncryption
Well hello there, this ctf is a crypto that i found in hack the box, and i said why not give it a go (looked interessting)

after downloading the directory and puting the password, i had 2 files, the first was this python code with the encryption function on it

![Image Description](/ctf0.png)

And the second on was this text message

![Image Description](/ctf1.png)

So i assumed that this text was the encrypted message used by the function above;
First of all i need to understand what does the python code do, so i can decrypt the message for the flag

![Image Description](/ctf3.png)

In the beggining the code 
- <b> takes a message ( In this case our flag ) <b> 
- <b> then he will create an empty list <b> 
- <b> Then for every caracter in the message, he will take that caracter and does the formula to cypher the message
- <b> And he will put that caracter in the list, as a hex

Example:

![Image Description](/ctf4.png)

will give us this 

![Image Description](/ctf5.png)

Now that i know how the code first, let's start by finding the reverse formula to decrypt the message

<h2> Formula </h2>

Let's suppose e representse the encrypted caractere and d is decrypted text, wish means we have:
- e = 123 * d + 18 mod 256
- Wish means that 123 * d + 18 = e mod 256
- 123 * d  = e -18 mod 256 and since -18 = 238 mod 256
-  123 * d = e + 238 mod 256
- now i need to find the 123 reverse value so when i multiply 123 by this reverse i'll have 123 * rev = 1 mod 256
- With some little calculations we find that 256 * 37 - 77 * 123 = 1 
- Wish means that -77 * 123 = 1 mod 256 -> 123 * 179 = 1 mod 256 ( since 179 = - 77 mod 256 )
- So we find that d = ( e + 238 ) * 179 mod 256

![Image Description](/ctf6.png)

<h2> Code </h2>
Now that i can decrypt the code i just need to create a program that will reverse the calculations

The first problem the i found was that i need to start from the last element ( i just realized after i finished the ctf that there was a more optimal function )
so i started by listing the elements from the last element to the first 

![Image Description](/ctf7.png)

What you should know is that the text was encrypted in hexadecimal, with two letters, for example if we do 156 in decimal is 16 * 9 + 12, wish means 9c in hexadeciaml,
so i will need to take 2 elements every time ( 9c for example ) and make it into an int, so this is what i came up with

![Image Description](/ctf8.png)

i take two caracteres every time and will make into and integer and then cast them into a caractere and append them to list

![Image Description](/ctf9.png)

At the end, i added this function line of code to reverse the message and put it out as a string and this is what i got when i used the text message in the code.

![Image Description](/ctfresultat.png)


![Image Description](/ctffinal.png)
