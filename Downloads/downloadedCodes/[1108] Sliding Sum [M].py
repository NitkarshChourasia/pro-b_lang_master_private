"""
####  Sliding Sum  ####

Create a function that returns the subarrays of n consecutive elements from the original element that sum up to k. The function will have the following form: sliding_sum(lst, n, k)
To illustrate:
___
sliding_sum([3, 4, 1, 9, 9, 0, 3, 5, 4], 3, 8) ➞ [[3, 4, 1], [0, 3, 5]]
# Where [3, 4, 1] and [0, 3, 5] are the only subarrays that sum to 8 with length 3.
_____



[Examples]

___
sliding_sum([1, 4, 2, 3, 5, 0], 2, 5) ➞ [[1, 4], [2, 3], [5, 0]]

sliding_sum([5, 5, 5, 5, 5], 1, 5) ➞ [[5], [5], [5], [5], [5]]

sliding_sum([5, 5, 5, 5, 5], 5, 24) ➞ []
_____



[Notes]

Return an empty array if no subarrays satisfy the (n,k) condition.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Snail Crawl out of the Bucket
https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
The yield keyword enables a function to comeback where it left off when it is called again. This is the critical difference from a regular function. A regular function …
_________

"""
#Your code should go here:

