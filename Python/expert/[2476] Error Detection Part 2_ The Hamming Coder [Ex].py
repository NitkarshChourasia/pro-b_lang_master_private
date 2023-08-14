"""
####  Error Detection Part 2: The Hamming Coder  ####

This challenge is a continuation of Error Detection Part 1: The Hamming Checker . To recap:
___
*) Every redundant bit in a Hamming block informs about the parity of the numbers of 1s inside its region: a 0 indicates an even number of 1s, and a 1 indicates an odd number of 1s.
*) Redundant bits are always placed in powers of two: index 1, 2, 4, etc., or binary 1, 10, 100, etc.
*) All indices inside a region are related to the index of the redundant bit for that region: for the redundant bit in position 0100 (decimal 4), the indices in its region are 0101, 0110, 0111, 1100, 1101, 1110 and 1111. Specifically, all these have a 1 for the third-to-last digit. This pattern applies to all regions: 
*) A block with m bits needs n redundant bits, where 2^n = m.
___

For this challenge, your task is to write a function that takes a Hamming block and fills in all the redundant bits with the appropriate value. The redundant bits are already in place, but they are all 0s.
This time, the bit indexed 0 will be put to use. This bit will encode information about the whole block, taking on the value (0 or 1) that makes the total number of 1s even. Using this extra bit allows the receiver to detect if there have been two errors, albeit not their positions.
Your code should work for blocks of different sizes (sizes will always be powers of two).


[Examples]

___
hamming_coder("0000010100011000") ➞ "0100110100011000"

hamming_coder("0000000001010000") ➞ "1010000001010000"

hamming_coder("00010111010110000111001110001010") ➞ "00110111010110000111001110001010"

hamming_coder("00000110001001000111010100100101") ➞ "10101110101001000111010100100101"
_____



[Notes]

___
*) Redundant bits always have powers of two as their indices.
*) Each region divides the block into two. Some regions divide the block vertically, with columns doubling in width; some others divide the block horizontally, with rows doubling in height. The redundant bits always sit at the top left corner of each region. Here's an example of how a block size 32 would be partitioned.
___



[bit_operations] [logic] 



-------------------------------------------------------------------
[Resources]
_________
int.bit_length()
https://www.geeksforgeeks.org/python-bit-functions-on-int-bit_length-to_bytes-and-from_bytes/
Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.
_________
_________
Python Bitwise Operators
https://www.geeksforgeeks.org/python-bitwise-operators/#:~:text=In%20Python%2C%20bitwise%20operators%20are,perform%20bitwise%20calculations%20on%20integers.&text=Bitwise%20AND%20operator%3A%20Returns%201,bit%20is%201%20else%200.
Are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwi …
_________

"""
#Your code should go here:

