"""
####  Error Detection Part 1: The Hamming Checker  ####

When a message, expressed as a long stream of 0s and 1s, is sent to you, one or more of its bits might get flipped on the way. If that's the case, it can be useful to have some way of figuring out if and where a "bit flip" happened so as to flip it back. One solution is to include in the message some form of meta-information about the message itself than can help you decide if the message has been corrupted or not.
Hamming code is a block of code that includes redundant bits in it. These bits are not to be considered part of the message itself but are used to tell if the non-redundant bits are fine, or if one has been flipped. As an illustration, consider a message with 16 bits:
___
0111
0010
1110
0100
_____

In this block, 4 bits are redundant and 11 carry the message (the bit in position 0 won't be used in this challenge). The redundant bits always have powers of two as their indices, so they occupy positions 1, 2, 4, and 8 here. The way they encode information about the message is:
___
*) Each redundant bit is in charge of checking a given region of the code.
*) The 1s inside each region are counted. If the number of 1s is odd, the redundant bit for that region is a 1 so as to make the count even. If it is already even, the redundant bit is a 0.
*) Each region divides the block in the following manner:
___


The red rectangles represent a region, and the redundant bit in charge of it is underlined for each of them. This block is probably uncorrupted since the number of 1s is even for all regions.
Your task is to write a function that takes a Hamming block and checks for corrupted bits. If the Hamming method finds no corrupted bits, return the same block as the input. If one corrupted bit is found, return the fixed code. For this challenge, there won't be more than one error per block.
Hint: Hamming blocks are designed so that the (number of 1s) mod 2 of all regions "spell out" the reversed index of the corrupted bit in binary. For example:
___
0110    region 1: 3 mod 2 = 1    corrupted bit: index 0011 (decimal 3)
0010    region 2: 3 mod 2 = 1
1110    region 3: 2 mod 2 = 0
0100    region 4: 4 mod 2 = 0
_____

In general, think of all indices in binary and you might find some interesting patterns.


[Examples]

___
hamming_checker("0100100100010010") ➞ "0100100000010010"
# The corrupted bit is in position 7.

hamming_checker("0011011010100110") ➞ "0010011010100110"
# The corrupted bit is in position 3.

hamming_checker("0010101011111111")  ➞ "0010101011111111"
# There are no corrupted bits.
_____



[Notes]

___
*) All blocks will be size 16.
*) There will be at most one bit flip per block.
*) For a visual explanation of this challenge and a possible solution, check out the videos in the Resource tab.
*) For more, check out part 2.
___



[bit_operations] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
What Does the % Symbol Mean in Python?
https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
Is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder of a division problem.
_________
_________
^ Bitwise Exclusive XOR
https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
Sets the bits in the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.
_________
_________
Applying Hamming Code to Blocks of Data
http://www.eecs.umich.edu/courses/eecs373.w05/lecture/hamming3.pdf
Hamming code affords a straightforward way to protect a block of data against single bit errors. It allows any single bit error to be detected and corrected. This discu …
_________
_________
Hamming Codes: The Elegance of It All
https://www.youtube.com/watch?v=b3NxrZOu_CE
A cleaner perspective on Hamming error correction codes.
_________
_________
Hamming Codes and Error Correction
https://www.youtube.com/watch?v=X8jsijhllIA
A discovery-oriented introduction to error correction codes.
_________

"""
#Your code should go here:

