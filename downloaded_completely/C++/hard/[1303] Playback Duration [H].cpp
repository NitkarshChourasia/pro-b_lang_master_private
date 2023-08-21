/*
####  Playback Duration  ####

YouTube offers different playback speed options for users. This allows users to increase or decrease the speed of the video content. Given the actual duration and playback speed of the video, calculate the playback duration of the video.


[Examples]

___
playbackDuration("00:30:00", 2) ➞ "00:15:00"

playbackDuration("01:20:00", 1.5) ➞ "00:53:20"

playbackDuration("51:20:09", 0.5) ➞ "102:40:18"
_____



[Notes]

___
*) Both durations will be in hh:mm:ss format.
*) Playback speed will be up to one decimal place only.
*) Time units are expected to be truncated/floored.
___



[conditions] [logic] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object.
_________
_________
floor()
https://www.programiz.com/cpp-programming/library-function/cmath/floor
Returns the largest possible integer value which is less than or equal to the given argument.
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val. The format used is the same that printf would print for the corresponding type.
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also sets …
_________

*/
//Your code should go here:

