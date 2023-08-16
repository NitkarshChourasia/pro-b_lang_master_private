"""
####  Learn Italian Verbs!  ####

Most Italian verbs fall into one of three categories: those ending in are, those ending in ere, and those ending in ire. How a verb is inflected depends on what category it belongs to.
A simple way to inflect an Italian verb is: delete the are/ere/ire ending to get the verb base, append a part specific to its category, and append a part common to all verbs. For example, this is the Present Simple of three verbs for the plural you (Italian voi):
___
*) Amare (To love): Voi amate (you love) ➞ Specific: a, common: te
*) Credere (To believe): Voi credete (you believe) ➞ Specific: e, common: te
*) Dormire (To sleep): Voi dormite (you sleep) ➞ Specific: i, common: te
___

Create a function that takes in three parameters and returns an inflected verb with the appropriate pronoun. The input will be an Italian verb, a person (first, second, third) and a number (singular, plural).
You'll be given three dictionaries: one with the Italian pronouns, one with the common part, and one with the specific part. For the first two, the number will be nested within the person. For the third, you will also find lists as values for the specific part of verbs ending in are, ere, and ire respectively.


[Examples]

___
inflect("amare", "first", "pl") ➞ "Noi amiamo"
# Pronoun: "Noi" + verb base: "am" + specific part: "ia" + common part: "mo"

inflect("credere", "third", "sing") ➞ "Lui/Lei crede"
# Pronoun: "Lui/Lei" + verb base: "cred" + specific part: "e" + common part: None

inflect("dormire", "sec", "pl") ➞ "Voi dormite"
# Pronoun: "Voi" + verb base: "dorm" + specific part: "i" + common part: "te"
_____



[Notes]

___
*) The dictionary for the pronouns is called pronomi.
*) The dictionary for the specific part is called verbi_spec.
*) The dictionary for the common part is called verbi_com.
*) You'll find all three in the Tests tab of your console. You can copy-paste them on your compiler to work with them, but don't include them in your submission.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Nested Dictionary
https://www.programiz.com/python-programming/nested-dictionary
In this article, you’ll learn about nested dictionary in Python. More specifically, you’ll learn to create nested dictionary, access elements, modify them and so on wit …
_________
_________
Splitting, Concatenating, and Joining Strings
https://realpython.com/python-string-split-concatenate-join/
In this beginner-friendly article, you’ll learn some of the most fundamental string operations: splitting, concatenating, and joining. Not only will you learn how to us …
_________

"""
#Your code should go here:

