/*
####  Find the Bug: Checking Even Numbers  ####

Create a function that takes in an array and returns true if all its values are even, and false otherwise.
Not a big deal, your friend says. He writes the following code:
___
bool checkAllEven(std::vector<int> v) {
 return (std::all_of(v.cbegin(), v.cend(), [](int i){ return i % 2 != 0; }))
}
_____

Fix the code above so that all tests pass:


[Examples]

___
checkAllEven([1, 2, 3, 4]) ➞ false

checkAllEven([2, 4, 6]) ➞ true

checkAllEven([5, 6, 8, 10]) ➞ false

checkAllEven([-2, 2, -2, 2]) ➞ true
_____



[Notes]

For help, check Resources or ask a question in the Comments.


[arrays] [bugs] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
all_of()
https://www.geeksforgeeks.org/stdall_of-in-cpp/
The C++ function is defined in <algorithm> library in STL. This function operates on whole range of array elements and can save time to run a loop to check each element …
_________
_________
Lambda Expressions
https://docs.microsoft.com/cpp/cpp/lambda-expressions-in-cpp?view=msvc-160
Is a convenient way of defining an anonymous function object (a closure) right at the location where it is invoked or passed as an argument to a function. Typically lam …
_________

*/
//Your code should go here:

