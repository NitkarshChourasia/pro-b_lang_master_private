/*
####  Middle Square Algorithm (PRNG)  ####

Create a class that returns 32-bit pseudo-random numbers using the middle square algorithm.


[Background]

Computers were built to be deterministic, which means every action it performs is 100% predictable. However, in the case of random number generation (RNG), this makes it hard to come up with "random" numbers. To circumvent this, many people have come up with pseudo-random number generators (PRNG) which generate numbers that seem random, but are still perfectly predictable if you know how the algorithm works. One of these algorithms is called the middle square algorithm.
PRNGs typically take in a "seed" as their initial state. Then, to generate a new random number, you perform some series of calculations on that state and then set the state to that new number. The middle square algorithm is no different -- it takes a seed and then performs a series of calculations to find the next number.
Let's say you want to generate two-digit random numbers. To generate a new number, start with your state:
___
85
_____

Square it:
___
85^2=7225
_____

and take the two middle digits:
___
22
_____

... to get the next random number.
Once you've retrieved the next number, store it into the state to be used later and then return it. You can repeat this as many times as you want to generate as many "random" numbers as needed:
___
22
22^2=0484 (pad the number with zeroes)
48 <- next random number
48^2=2304
30 <- next random number
30^2=0900
90 <- next random number
90^2=8100
10 <- next random number
10^2=0100
10 <- next random number
_____

This particular number is important since we've generated the number 10 twice now. Because of how the algorithm works, this means that the generator will start infinitely generating tens.


[Instructions]

For this challenge, instead of generating two-digit decimal numbers, we'll be generating 32-bit binary numbers. Example:
___
00101000010100001010110110000010 (equal to 676,375,938)
0000011001011001010011111010010110000110110110001111011000000100 (equal to 457,484,409,505,379,844)
01001111101001011000011011011000 (digits 16-48; equal to 1,336,248,024) <- next random number
_____

Your task is to create a MiddleSquarePRNG class with the following methods:
___
*) void seed(int newSeed) -- set the state to newSeed
*) int next() -- return the next pseudo-random number
___



[Examples]

___
MiddleSquarePRND rand = new MiddleSquarePRND();
rand.seed(6492);
assert rand.next() == 643;
assert rand.next() == 6;
assert rand.next() == 0;
assert rand.next() == 0;
_____



[Notes]

___
*) You might want to store the state as a long instead of an int to square it.
*) Remember that the next() method returns an int and not a long!
*) Bit operations could help here.
*) Don't worry about signs ⁠— none of the numbers will get big enough to use them.
*) I've tried to organize the tests to make them easier to read at first glance.
*) This is not a good method of generating pseudo-random numbers!
___



[algorithms] [bit_operations] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Middle-Square Method
https://en.wikipedia.org/wiki/Middle-square_method
A method of generating pseudorandom numbers. In practice it is not a good method, since its period is usually very short and it has some severe weaknesses; repeated eno …
_________

*/
//Your code should go here:

