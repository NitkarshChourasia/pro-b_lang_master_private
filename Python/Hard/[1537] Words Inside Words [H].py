"""
####  Words Inside Words  ####

Words can be grouped together when one word can be found within another (e.g. eat is in heat and theater). Given a list of words, return a dictionary that groups together each word with a list of all other words that contain it. Each group of words should be returned in alphabetical order.


[Examples]

___
word_groups(["grates", "rat", "rates", "rations"]) ➞ {
  "rates": ["grates"],
  "rat": ["grates", "rates", "rations"]
}

word_groups(["duct", "produce", "product", "rod"]) ➞ {
  "duct": ["product"],
  "rod": ["produce", "product"]
}

word_groups(["her", "the", "here", "other", "there"]) ➞ {
  "the": ["other", "there"],
  "here": ["there"],
  "her": ["here", "other", "there"]
}
_____



[Notes]

Words can belong to more than one group.


[arrays] [conditions] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

