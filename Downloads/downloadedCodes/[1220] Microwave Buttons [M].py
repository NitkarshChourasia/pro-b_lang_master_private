"""
####  Microwave Buttons  ####

In microwave ovens, when buttons are pressed from 0-9, it will add that number to the microwave oven timer (starting from the left). All microwave ovens have the functionality where you can hit a "+30" button and it will add 30 seconds to the timer to cook your food. If you want to heat something for 5 mins, you can hit the "+30" button 10 times instead of thinking if there are fewer button presses that can give you the same result.
Create a function that takes an argument time and returns the shortest amount of button presses to set the given time on the microwave oven. The microwave oven timer always starts at 00:00.


[Buttons]

___
Buttons from "0-9"

# It will add that number to the microwave oven timer (starting from the left).
# If the number "5" is pressed followed by "0" twice, it will put 05:00 on the timer.
# If the number "3" is pressed followed by "0", it will put 00:30 on the timer.

Button "+30", which adds 30 seconds to the current timer.

# If the number "+30" is pressed twice, it will put 00:60 on the timer.

A "Start" button which you have to finally press to start the microwave oven.

# Remember to press this!
_____



[Examples]

___
microwave_buttons("00:30") ➞ 2
# "+30" to put 30 seconds on the timer.
# "Start" button to start the oven.

microwave_buttons("00:70") ➞ 3
# "7" followed by "0" to put 70 seconds on the timer.
# "Start" button to start the oven.

microwave_buttons("00:00") ➞ 1
# "Start" button to start the oven.
_____



[Notes]

___
*) Input may not always be what you expect (e.g. you can put in 00:70, which is valid).
*) No exception handling is required for this challenge.
___



[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.datacamp.com/community/tutorials/python-string-split?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=21452&gclid=CjwKCAiAwrf-BRA9EiwAUWwKXhavf52Rz_lDTIeASiCKFzokq9D-CbyKVoOnGgYmvI3LFxfsQUFxfxoCfzgQAvD_BwE
Inputs a string value and outputs a list of words contained within the string by separating or splitting the words on all the whitespaces by default. It also has an opt …
_________
_________
String lstrip() Method
https://www.w3schools.com/python/ref_string_lstrip.asp
Removes any leading characters (space is the default leading character to remove).
_________

"""
#Your code should go here:

