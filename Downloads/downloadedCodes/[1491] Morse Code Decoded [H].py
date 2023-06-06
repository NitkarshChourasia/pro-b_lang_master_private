"""
####  Morse Code Decoded  ####

Create a function that takes a string (morse code) as an argument and returns an unencrypted string.


[Examples]

___
decode_morse(".... . .-.. .--.   -- .   -.-.--") ➞ "HELP ME !"

decode_morse("-.-. .... .- .-.. .-.. . -. --. .") ➞ "CHALLENGE"

decode_morse(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .") ➞ "EDABBIT CHALLENGE"
_____

The following dict can be used for coding:
___
morse_to_dots = {
  "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
  "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
  "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
  "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
  "Y": "-.--", "Z": "--..", "0": "-----",
  "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
  "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
  ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-",
  "-": "-....-", "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-."
}

dots_to_morse = {}
for key, val in morse_to_dots.items():
    dots_to_morse[val] = key
_____



[Notes]

___
*) Return values are all uppercase.
*) Input string can have digits.
*) Input string can have some special chararacters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
___



[arrays] [conditions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
International Morse Code
https://morsecode.scphillips.com/morse2.html
International Morse code: all letters, digits, accented letters and punctuation marks are tabulated along with the common prosigns, Q codes and abbreviations.
_________

"""
#Your code should go here:

