"""
####  Help the Hanoi Monks With Their Towers  ####

There is a legend that near the city of Hanoi in Vietnam there is a monastery with a bronze plate and three rods on it.
At the creation of the world, God strung 64 disks of various diameters of pure gold on the first rod. He placed the largest disk on the plate, and put each smaller disk on a larger one.
There was a prophecy that the moment the monks of the monastery transfer all these 64 disks from the first rod to the third, the end of the world will come and eternal bliss will come for the righteous. Therefore, the monks work day and night, carrying disks. But the work is progressing very slowly because the monks have to follow two simple rules:

The monks have been given a 600 billion year deadline to finish their work. But they have already fallen behind schedule because sometimes they get lost in their calculations, and for a long time can not decide which disk to move and where.
Help the monks. Write a function that, having received the move number, will show how to perform this move. The function has to return a tuple of three numbers:
___
*) Disk number.
*) Rod number from which to take the disk.
*) Rod number where to put this disk.
___

Disks are numbered from 1 (smallest disk) to 64 (largest disk).


[Examples]

___
hanoi(1) ➞ (1, 1, 2)

hanoi(2) ➞ (2, 1, 3)

hanoi(2**63) ➞ (64, 1, 3)

hanoi(15215285751613538304) ➞ (15, 2, 3)
_____



[Notes]

On the average computer, Python will take about 50 thousand years to go through all the disk moving. Therefore, instead of running over all the disk moves, it's necessary to find a pattern of moves.



[algebra] [algorithms] [logic] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

