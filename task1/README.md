90The Problem:
Given an integer num, return a string representing its hexadecimal representation. 
The Solution:
Firstly we used a dictionary of key and value the key represents if the number is equal to or greater than 10 and the value represents the correspending hexadecimal format for the number for example 10 = a and so on 
Secondly if the number equals 0 the answer will be zero
Thirdly if the number is less than 1 (negative number) we used two’s complement method 
Then we used a while loop and its structue is when the number is greater than 1 (poistive number) we and if the modulus of this number is less than 10 we divide the number by 16 and convert it to string and add it to our result list , and else (greater than 10) we divide the number by 16 and get its corresponding value from the dictionary we made.
 


