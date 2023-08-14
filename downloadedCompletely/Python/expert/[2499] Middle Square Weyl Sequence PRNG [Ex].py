"""
####  Middle Square Weyl Sequence PRNG  ####

The middle-square method is a method of generating pseudorandom numbers. In practice, it's not a good method, since its period is usually very short and it has some severe weaknesses. The defects associated with the original middle-square generator can be rectified by running the middle square with a Weyl sequence, which prevents convergence to zero.
Write a function msws(seed, n) that can generate the n-th random 16-bit long number. The implementation should result in fast performance.
Algorithm description:
___
*) raise r to the power of 2
*) update weyl number by adding marsaglia
*) add weyl to r
*) drop 8 bits from the right, extract 16 bits from the right to get new random r
___

___
marsaglia = 362437
r, weyl = seed, 0

# repeat n times to get n-th random number r:
r = r ** 2
weyl = (weyl + marsaglia) % 2 ** 32
r = (r + weyl) % 2 ** 32
r = (r // 2 ** 8) % 2 ** 16
_____



[Examples]




[Notes]

___
*) The function should be efficient to handle large n (be inventive).
*) For comparison, my submitted solution takes less than a second to complete all tests.
*) Hint: a compiled program can run up to 200 times faster than a mathematically identical script in the Python interpreter.
*) The code in Tests makes a temporary directory that will exist only during the execution of the tests.
___



[algorithms] [bit_operations] [math] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

