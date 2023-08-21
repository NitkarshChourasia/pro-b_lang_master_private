/*
####  Polybius Square, Bifid Cipher  ####

The basic Polybius Square is a 5x5 square grid with the letters A-Z written into the grid. "I" and "J" typically share a slot (as there are 26 letters and only 25 slots).

The Bifid cipher uses the Polybius square but adds a layer of complexity.
Start with a secret message. Remove spaces and punctuation.
___
plaintext = "ikilledmufasa"
_____

Encipher the message using the basic Polybius cipher (see my previous challenge — right click and select "open in new tab"), but write the numbers in two rows under the message, like so:

Read off the numbers horizontally, in pairs:
___
22 23 31 13 42 14 14 54 11 54 25 11 31
_____

Generate the ciphertext by converting these new pairs of numbers into new letters using the Polybius square.
___
ciphertext = "ghlcrddyaykal"
_____

Create a function that takes a plaintext or ciphertext, and returns the corresponding ciphertext or plaintext.


[Examples]

___
bifid("I killed Mufasa!") ➞ "ghlcrddyaykal"

bifid("ghlcrddyaykal") ➞ "ikilledmufasa"

bifid("hi") ➞ "go"
_____



[Notes]

N/A


[arrays] [cryptography] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Bifid Cipher
http://practicalcryptography.com/ciphers/bifid-cipher/
Bifid is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion. It was invented by Felix Delastelle. Delastelle wa …
_________
_________
Polybius Square
https://en.wikipedia.org/wiki/Polybius_square
Is a device invented by the ancient Greeks Cleoxenus and Democleitus, and made famous by the historian and scholar Polybius.
_________
_________
Bifid Cipher
https://en.wikipedia.org/wiki/Bifid_cipher#:~:text=In%20classical%20cryptography%2C%20the%20bifid,around%201901%20by%20Felix%20Delastelle.
Is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion. It was invented around 1901 by Felix Delastelle.
_________

*/
//Your code should go here:

