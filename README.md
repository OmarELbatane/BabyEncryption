# BabyEncryption
Well hello there, this ctf is a crypto that i found in hack the box, and i said why not give it a go (looked interessting)

after downloading the directory and puting the password, i had 2 files, the first was this python code with the encryption function on it

![Image Description](/ctf0.png)

And the second on was this text message

![Image Description](/ctf1.png)

So i assumed that this text was the encrypted message used by the function above;
First of all i need to understand what does the python code do, so i can decrypt the message for the flag

![Image Description](/ctf0.png)

In the beggining the code 
- <b> takes a message ( In this case our flag ) <b> 
- <b> then he will create an empty list <b> 
- <b> Then for every caracter in the message, he will take that caracter and does the formula to cypher the message
- <b> And he will put that caracter in the list, as a hex
Example
 ![Image Description](/ctf4.png)

will give us this 

![Image Description](/ctf5.png)

![Image Description](/ctfresultat.png)


![Image Description](/ctffinal.png)
