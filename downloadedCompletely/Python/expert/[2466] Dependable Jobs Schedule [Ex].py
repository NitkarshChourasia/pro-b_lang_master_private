"""
####  Dependable Jobs Schedule  ####

The function is given the number of jobs and a list of prerequisites. Each job is labeled from 0 to jobs - 1. The list of dependencies has lists of pairs [j, i] meaning that job j can start after the job i has been completed. A job can depend on multiple jobs to be completed or have no dependencies at all. If a job is not dependent on another job, it can be completed immediately. Given the dependencies, determine if all jobs can be finished and return True / False.


[Examples]

___
finish_all(2, [[1, 0]]) ➞ True
# job-0 has no dependency and can be finished.
# job-1 depends on job-0, so it can also be finished.

finish_all(2, [[1, 0], [0, 1]]) ➞ False
# Neither job-0 nor job-1 can be finished because they are mutually dependent.

finish_all(3, [[1, 0], [2, 1]]) ➞ True
# The jobs are sequentially dependent.

finish_all(4, [[0, 1], [1, 2], [2, 0]]) ➞ False
# Circular dependence between 0-1-2-0 prevents them from being finished.

finish_all(1, []) ➞ True
# Only one job-0 with no dependence.
_____



[Notes]

The list of prerequisites has dependencies within the given range of jobs.


[algorithms] [conditions] [games] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

