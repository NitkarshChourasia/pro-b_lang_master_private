/*
####  Stock Picker  ####

Create a function that takes an array of integers that represent the amount in dollars that a single stock is worth, and return the maximum profit that could have been made by buying stock on day x and selling stock on day y where y>x.
If given the following array:
___
[44, 30, 24, 32, 35, 30, 40, 38, 15]
_____

... your program should return 16 because at index 2 the stock was worth $24 and at the index 6 the stock was then worth $40, so if you bought the stock at 24 and sold it on 40, you would have made a profit of $16, which is the maximum profit that could have been made with this list of stock prices.
If there is no profit that could have been made with the stock prices, then your program should return -1 (e.g. [[10, 9, 8, 2]] should return -1).


[Examples]

___
stockPicker([10, 12, 4, 5, 9]) ➞ 5

stockPicker([14, 20, 4, 12, 5, 11]) ➞ 8

stockPicker([80, 60, 10, 8]) ➞ -1
_____



[Notes]

N/A


[algorithms] [arrays] [data_structures] 



-------------------------------------------------------------------
[Resources]
_________
max_element
https://www.geeksforgeeks.org/max_element-in-cpp/
We have std::max to find maximum of 2 or more elements, but what if we want to find the largest element in an array or vector or list or in a sub-section. To serve this …
_________
_________
Filter Out Elements From std::vector
https://codereview.stackexchange.com/questions/175713/filter-out-elements-from-stdvector
Filter out elements from std::vector.
_________
_________
Maximum Subarray Problem
https://en.wikipedia.org/wiki/Maximum_subarray_problem
This problem can be reduced to maximum subarray problem by considering an array of adjacent elements differences. It can be solved in linear time and constant space.
_________

*/
//Your code should go here:

