/*
####  Edabit's Encryption Scheme  ####

An English text needs to be encrypted using Edabit’s encryption scheme. First, the spaces are removed from the text. Let L be the length of this text. Then, characters are written into a grid, whose rows and columns have the following constraints:
For example, the sentence "if man was meant to stay on the ground god would have given us roots", after removing spaces, is 54 characters long. The square root of 54 is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.
___
ifmanwas
meanttos
tayonthe
groundgo
dwouldha
vegivenu
sroots
_____

___
*) Ensure that rows x column >= L
*) If multiple grids satisfy the above conditions, choose the one with the minimum area.
___

___
rows x columns >= L
_____

The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:
___
imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
_____



[Examples]

___
encryption(“haveaniceday”) ➞ “hae and via ecy”

// have
// anic
// eday

encryption(“feedthedog”) ➞ “fto ehg ee dd”

encryption(“chillout”) ➞ “clu hlt io”

encryption(“A Fool and His Money Are Soon Parted.”) ➞ "Anoea FdnSr oHeot oiyoe lsAnd aMrP."
_____



[Notes]

___
*) Ensure capitalization remains the same in encrypted text.
*) Do not remove special characters.
___



[cryptography] [loops] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to replace all occurrences of a character in string?
https://stackoverflow.com/questions/2896600/how-to-replace-all-occurrences-of-a-character-in-string
What is the effective way to replace all occurrences of a character with another character in std::string?
_________

*/
//Your code should go here:

