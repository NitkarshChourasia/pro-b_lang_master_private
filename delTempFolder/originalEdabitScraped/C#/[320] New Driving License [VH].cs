/*
####  New Driving License  ####

You have to get a new driver's license. You show up at the office at the same time as four other people. The office says they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out with your new license?
Your input will be a string of your name me, an integer of the number of available agents, and a string of the other four names separated by spaces others.
Return the number of minutes it will take to get your license.


[Examples]

___
License("Eric", 2, "Adam Caroline Rebecca Frank") ➞ 40
// As you are in the second group of people.

License("Zebediah", 1, "Bob Jim Becky Pat") ➞ 100
// As you are the last person.

License("Aaron", 3, "Jane Max Olivia Sam") ➞ 20
// As you are the first.
_____



[Notes]

N/A


[arrays] [logic] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
How to round up the result of integer division?
https://stackoverflow.com/questions/17944/how-to-round-up-the-result-of-integer-division
AFAICS, this doesn't have the overflow bug that Brandon DuRette pointed out, and because it only uses it once, you don't need to store the recordsPerPage specially if i …
_________

*/
//Your code should go here:

