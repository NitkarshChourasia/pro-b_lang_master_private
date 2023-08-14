"""
####  Fancy a Dictionary? Give it a Trie!  ####

A trie is a specialized type of tree data structure. When used in the context of a dictionary, each node stores the entire alphabet, and words can be reTRIEved by traversing down a branch part of the tree. The structure of a trie tree is a set of linked tries emanating from a head trie. Each trie contains a set of pointers (child tries), one for each alphabetic value.
The image below gives a representation of how a trie dictionary might store the words peter, piper, picked, peck, pickled, and peppers. For simplicity, most of the child nodes are omitted but the tree hierarchy can be readily seen and how a letter at a given level branches out (e.g p, pe, etc).

What is not clear is how the end of a word is recognized. There are many ways to do this, but for a simple dictionary, it is sufficient to have a flag indicating if the trie represents the end of a word or not. Hence a word proceeds letter by letter from the head trie. As the words are unique, the full path for any individual word is also unique, although paths are shared where common (think how "help" and "helpless" would be represented).
For this challenge, we are going to construct a Trie class which can hold a set of lower case English letter words, together with methods and a function to allow it to be used in a basic way:
___
*) Function load(words) ⁠— words is a list of words that will be the initial set for the dictionary. The function should create the trie, load the words then return a pointer to the head trie.
*) Instance method update(self, words) ⁠— This adds any words in the list words which are not already contained in the dictionary.
*) Instance method is_word(self, word) ⁠— Returns True if word is in the dictionary, otherwise False.
*) Instance method remove(self, word) ⁠— Removes word from the dictionary if it's present, otherwise no action.
*) Instance method contents(self, start="a", end="z") ⁠— Returns a list of all or some of the words in the dictionary in ascending alphabetical order. If the start and/or end is present, only return the words which start with the letters between the start and end inclusive. start and end should be validated to ensure end is not before start; if it is, return the string "End cannot be earlier in the alphabet than start". If the dictionary is empty, return the string "Dictionary is currently empty".
*) Class/static method num_words() ⁠— Should return the number of words currently in the dictionary. If the dictionary is empty, return the string "Dictionary is currently empty".
___



[Examples]

___
d = load(["Peter", "Piper", "picked", "peppers"])
d.contents() ➞ ["peppers", "peter", "picked", "piper"]
d.num_words() ➞ 4
d.remove("peppers")
d.is_word("peppers") ➞ False
Trie.num_words() ➞ 3
d.update(["pineapples"])
d.contents("p","p") ➞ ["peter", "picked", "pineapples", "piper"]
_____



[Notes]

___
*) Although words are stored in lower case in the dictionary, words input to load, update and is_word may contain capitals. The word lists input to load and update may also contain duplicates.
*) Take extra care with the remove method ⁠— if you are removing "hope", for example, you need to be sure you can still access "hopeful" if that's present.
___



[classes] [data_structures] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Trie Data Structure
https://www.youtube.com/watch?v=TRg9DQFu0kU
Good overview taken from this excellent course on youtube.
_________
_________
Trying to Understand Tries
https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
There are a handful of different ways to represent something as seemingly simple as a set of words. For example, a hash or dictionary is one that we’re probably familia …
_________

"""
#Your code should go here:

