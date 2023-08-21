/*
####  Dependable Jobs Schedule  ####

The function is given the number of jobs and an array of prerequisites. Each job is labeled from 0 to jobs - 1. The array of dependencies has arrays of pairs [j, i] meaning that job j can start after the job i has been completed. A job can depend on multiple jobs to be completed or have no dependencies at all. If a job is not dependent on another job, it can be completed immediately. Given the dependencies, determine if all jobs can be finished and return true / false.


[Examples]

___
finishAll(2, [[1, 0]]) ➞ true
// job-0 has no dependency and can be finished.
// job-1 depends on job-0, so it can also be finished.

finishAll(2, [[1, 0], [0, 1]]) ➞ false
// Neither job-0 nor job-1 can be finished because they are mutually dependent.

finishAll(3, [[1, 0], [2, 1]]) ➞ true
// The jobs are sequentially dependent.

finishAll(4, [[0, 1], [1, 2], [2, 0]]) ➞ false
// Circular dependence between 0-1-2-0 prevents them from being finished.

finishAll(1, []) ➞ true
// Only one job-0 with no dependence.
_____



[Notes]

The array of prerequisites has dependencies within the given range of jobs.


[algorithms] [conditions] [games] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Vector of Vectors
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________

*/
//Your code should go here:

