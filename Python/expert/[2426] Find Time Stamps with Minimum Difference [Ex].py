"""
####  Find Time Stamps with Minimum Difference  ####

The function is given an unsorted list of timestamps as strings in military format: "00:00:00" -> "23:59:59". Find two timestamps that have a minimum duration between them among all possible pairs from the list. It's possible that more than one pair can have the minimum duration. Thus return the set of tuples, e.g. {(t1, t2), (t3, t4), etc}.
The digital clock still goes around the clock, which is important for duration calculation. For example:
___
*) t1 = "23:59:59"
*) t2 = "00:00:01"
___

Then (t1, t2) has duration of 2 seconds, while (t2, t1) has duration of 24 * 3600 - 2 seconds.


[Examples]

___
min_time_diff(["01:10:00", "02:15:30", "01:10:10"]) ➞ {('01:10:00', '01:10:10')}

min_time_diff(["23:59:59", "14:35:30", "00:00:00"]) ➞ {('23:59:59', '00:00:00')}

min_time_diff(["23:59:25", "23:59:57", "17:20:30", "00:00:02", "17:20:35"]) ➞ {('23:59:57', '00:00:02'), ('17:20:30', '17:20:35')}

min_time_diff(["00:00:08", "00:00:04", "00:00:12"]) ➞ {('00:00:08', '00:00:12'), ('00:00:04', '00:00:08')}
_____



[Notes]

N/A


[algorithms] [arrays] [dates] [strings] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

