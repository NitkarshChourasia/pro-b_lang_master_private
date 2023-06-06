"""
####  Name Count Equality  ####

Create a function that counts the embedded names in the string and determines the equality. The names are embedded in a string of mixed special symbols and characters. The names to be counted to are adjoined with the ampersand symbol & and as the second parameter. See the following examples for more details.


[Examples]

___
equal_count("Peter!@#$Paul&*#Peter!--@|#$Paul#$Peter@|Paul$%^^Peter++Paul%$%^Peter++Paul#$#$#Peter@|Paul", "Peter&Paul")
➞ {"Peter":6, "Paul": 6, "equality": True}

equal_count("Elliot!@#$Sam!--@|#$Elliot@|Sam++Elliot$%^Elliot@|Sam!@#Elliot!@#$Sam!--@|#$Elliot", "Sam&Elliot")
➞ {"Sam": 4, "Elliot": 6, "equality": False, "difference": 2}
# "difference" key is added if count is not equal.

equal_count("Tim!@#$Kit&&*#Tim!--@|#$Kit#$%Tim@|Kit$%^^Tim++Kit%$%^Tim++Kit#$#$#Tim@|Kit", "Ken&Tom")
➞ {"Ken": 0, "Tom": 0, "equality": True}
_____



[Notes]

Make sure to return the result as a dict with the corresponding keys seen in the above examples and the difference key when needed.


[objects] [strings] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

