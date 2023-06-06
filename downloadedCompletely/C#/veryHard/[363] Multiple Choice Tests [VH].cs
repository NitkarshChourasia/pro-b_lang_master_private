/*
####  Multiple Choice Tests  ####

Your task is to write a program which allows teachers to create a multiple choice test in a class called Testpaper and also be able to assign a minimum pass mark. The Testpaper class should implement the ITestpaper interface given in the code template which has the following properties:

Interfaces do not define constructors for classes which implement them so you will need to add a constructor method which takes the parameters (string subject, string[] markScheme, string passMark).
As well as that, we need to create student objects to take the test itself! Create another class called Student which implements the given IStudent interface which has the following members:



[Examples]

___
paper1 = new Testpaper("Maths", new string[] { "1A", "2C", "3D", "4A", "5A" }, "60%")
paper2 = new Testpaper("Chemistry", new string[] { "1C", "2C", "3D", "4A" }, "75%")
paper3 = new Testpaper("Computing", new string[] { "1D", "2C", "3C", "4B", "5D", "6C", "7A" }, "75%")

student1 = new Student()
student2 = new Student()
_____

___
student1.TestsTaken ➞ { "No tests taken" }
student1.TakeTest(paper1, new string[] { "1A", "2D", "3D", "4A", "5A" })
student1.TestsTaken ➞ { "Maths: Passed! (80%)" }

student2.TakeTest(paper2, { "1C", "2D", "3A", "4C" })
student2.TakeTest(paper3, { "1A", "2C", "3A", "4C", "5D", "6C", "7B" })
student2.TestsTaken ➞ { "Chemistry: Failed! (25%)", "Computing: Failed! (43%)" }
_____



[Notes]

___
*) Round percentages to the nearest whole number.
*) Remember that the property TestsTaken should return { "No tests taken" } when no tests have been taken yet.
*) When one or more tests have been taken the TestsTaken property should return a string array sorted in alphabetical order of subject in the format shown above.
___



[classes] [formatting] [language_fundamentals] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Interfaces
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/interfaces/
Contains definitions for a group of related functionalities that a non-abstract class or a struct must implement. An interface may define static methods, which must hav …
_________
_________
Classes
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/classes
A type that is defined as a class is a reference type. At run time, when you declare a variable of a reference type, the variable contains the value null until you expl …
_________

*/
//Your code should go here:

