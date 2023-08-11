"""
####  The Trains Are Delayed Again  ####

Due to unforseen circumstances in Suburbia, the trains will be delayed by a further 10 minutes.
Create a function that will help to plan out and manage these delays! Create a function called manage_delays that does the following:
___
*) Parameters will be the train object, a destination and number of minutes the delay is.
*) Increment to the train object's expected_time by the delay, if the destination given is in the train object's destinations.
___



[Examples]

___
trains = [
  Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
  Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
  Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
]
_____

___
for t in trains:
    manage_delays(t, "Lakeside Valley", 60)

trains[0].expected_time ➞ "13:04"

trains[1].expected_time ➞ "14:20"

trains[2].expected_time ➞ "14:22"
_____



[Notes]

___
*) Keep in mind that times will be given in 24 hour time.
*) A train has the attributes destinations and expected_time. See the Tests tab for further details.
___



[classes] [dates] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Ending Time with 24 Hour Clock Logic with Leading Zeros
https://stackoverflow.com/questions/18642256/python-ending-time-with-24-hour-clock-logic-with-leading-zeros
I am close to a solution to this problem which reads: This program takes two lines of input. The first line is a "starting time" expressed in a 24-hour clock with lead …
_________

"""
#Your code should go here:

