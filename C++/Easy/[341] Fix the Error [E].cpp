/*
####  Fix the Error  ####

Create a function that returns true if two arrays contain identical values, and false otherwise.
To solve this question, your friend writes the following code:
___
bool checkEquals(std::vector<int> arr1, std::vector<int> arr2) {
    for (int i=0; i<arr1.size(); i++)
    {
    if (arr1[i]==arr2[i]){return false;}
    }
  return true;
}
_____

But testing the code, you see that something is not quite right. Running the code yields the following results:
___
checkEquals([1, 2], [1, 3]) ➞ false
// Good so far...

checkEquals([1, 2], [1, 2]) ➞ false
// Yikes! What happened?
_____

Rewrite your friend's code so that it correctly checks if two arrays are equal. To be equal, the arrays must have the same elements in the same order. The tests below should pass:


[Examples]

___
checkEquals([1, 2], [1, 3]) ➞ false

checkEquals([1, 2], [1, 2]) ➞ true

checkEquals([4, 5, 6], [4, 5, 6]) ➞ true

checkEquals([4, 7, 6], [4, 5, 6]) ➞ false
_____



[Notes]

N/A


[bugs] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
equal
http://www.cplusplus.com/reference/algorithm/equal/
Compares the elements in the range [first1,last1) with those in the range beginning at first2, and returns true if all of the elements in both ranges match.
_________

*/
//Your code should go here:

