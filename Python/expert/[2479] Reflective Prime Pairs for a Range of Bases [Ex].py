"""
####  Reflective Prime Pairs for a Range of Bases  ####

Find how many reflective prime pairs exist in a given range for each base in a given range. You'll be given two integers as parameters — ceiling range for primes and ceiling range for bases (ranges include the parameters). By "reflective" I mean two distinct numbers who are each other's reflection in the same base (e.g. 37 and 73).
Palindromic numbers like 101 don't count as reflective pairs with themselves — their pair must be distinct. Return a dictionary where ascending bases are keys and the count of reflective pairs within each are the values.
e.g.
___
{ base : count of reflective pairs for base, ... }
_____



[Examples]

___
prime_reflections(100, 5) ➞ {2: 6, 3: 6, 4: 4, 5: 6}

prime_reflections(10, 7) ➞ {2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0}

prime_reflections(1000, 11) ➞ {2: 45, 3: 33, 4: 30, 5: 39, 6: 10, 7: 28, 8: 13, 9: 28, 10: 18, 11: 38}
_____



[Notes]

prime_reflections(24, 7) means you should find all the positive prime numbers less than or equal to 24, then print out how many reflective pairs exist among these primes for the range expressed in bases 2 through 7 (we exclude base 1).


[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

