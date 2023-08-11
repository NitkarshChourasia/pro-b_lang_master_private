/*
####  Pages and Chapters  ####

Write a function that returns the closest chapter to the current page you are at. If two chapters are similarly close, return whichever has the higher page.


[Examples]

___
closestToPage(new ArrayList<Map.Entry<String, Integer> >(
  Arrays.asList(
      new SimpleEntry<String, Integer>("Chapter 1", 1),
      new SimpleEntry<String, Integer>("Chapter 2", 15),
      new SimpleEntry<String, Integer>("Chapter 3", 37)  
)), 10) ➞ "Chapter 2"


closestToPage(new ArrayList<Map.Entry<String, Integer> >(
  Arrays.asList(
      new SimpleEntry<String, Integer>("Chapter 1", 1),
      new SimpleEntry<String, Integer>("Chapter 2", 15),
      new SimpleEntry<String, Integer>("Chapter 3", 37)
)), 200) ➞ "The End?"


closestToPage(new ArrayList<Map.Entry<String, Integer> >(
  Arrays.asList(
      new SimpleEntry<String, Integer>("Chapter 1a", 1), 
      new SimpleEntry<String, Integer>("Chapter 1b", 5)
)), 3) ➞ "Chapter 1b"
_____



[Notes]

___
*) All page numbers in the book are valid integers.
*) Return the higher page number if ever two pages are equidistant (see test case #8).
*) The challenge introduces the use of Map.Entryand SimpleEntry classes in lieu to Map and HashMap.
*) Another version of this challenge which uses custom classes instead of Map-types can be found via this link.
___



[arrays] [numbers] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Map.Entry
https://docs.oracle.com/javase/8/docs/api/java/util/Map.Entry.html
Returns a collection-view of the map, whose elements are of this class. The only way to obtain a reference to a map entry is from the iterator of this collection-view. …
_________
_________
How to loop ArrayList
https://beginnersbook.com/2013/12/how-to-loop-arraylist-in-java/
Earlier we shared ArrayList example and how to initialize ArrayList in Java. In this post we are sharing how to iterate (loop) ArrayList in Java.
_________

*/
//Your code should go here:

