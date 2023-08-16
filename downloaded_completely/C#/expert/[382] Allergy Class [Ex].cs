/*
####  Allergy Class  ####

Create an Allergies class that holds a person's name and the things s/he is allergic to. Each allergy has a unique score value as follows:

By combining the scores for each allergy suffered by a person their overall allergy score is obtained. For example, if someone was allergic to Peanuts, Tomatoes, and Pollen, their allergy score would be 2 (Peanuts) + 16 (Tomatoes) + 64 (Pollen) their allergy score would be 82.
An enumeration type enum called Allergen is already declared in the Code tab and should not be altered.
The class should have the following members:


[Constructors]

One or more constructors allowing the following instantiations:
___
var mary = new Allergies("Mary") ➞ Mary initially has no allergies

var joe = new Allergies("Joe", 65) ➞ Joe is allergic to Eggs (1) and Pollen (64)

var rob = new Allergies("Rob", "Peanuts Chocolate Cats Strawberries") ➞ Rob is allergic to Peanuts, Strawberries, Chocolate, and Cats.
_____



[Properties (readonly)]

___
Name ➞ the name of the person
Score ➞ returning an `int` value equal to the allergy score
_____



[Methods]

___
*) ToString() ⁠— (override) returns a string in one of the following forms

"Mary has no allergies!"
"Fred is allergic to Peanuts."
"Joe is allergic to Eggs and Pollen."
"Rob is allergic to Peanuts, Strawberries, Chocolate, and Cats."
*) IsAllergicTo() ⁠— taking either a string parameter (e.g. "Pollen") or an Allergen enum value and returning true or false depending on whether the person is allergic to the given allergen.
*) AddAllergy() ⁠— taking string or Allergen parameter as above and updating the Score property by adding the numeric value of the given allergen.
*) DeleteAllergy() ⁠— taking string or Allergen parameter as above and updating the Score property by subtracting the numeric value of the given allergen.
___



[Notes]

___
*) The ToString() method should return the allergies in order of their score value
*) Check the Resources tab for links to helpful information.
*) The allergies string input to the constructor, as above will be space-separated and each word will match precisely to the name of one of the Allergen enum values.
*) This is the first challenge I've created from scratch, please leave comments for improvements or errors.
___



[bit_operations] [classes] [formatting] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Constructor Overloading
https://www.tutorialspoint.com/constructor-overloading-in-chash#:~:text=When%20more%20than%20one%20constructor,with%20Constructor%20Overloading%20in%20C%23.
When more than one constructor with the same name is defined in the same class, they are called overloaded, if the parameters are different for each constructor.
_________
_________
Classes
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/classes
A type that is defined as a class is a reference type. At run time, when you declare a variable of a reference type, the variable contains the value null until you expl …
_________
_________
Method Overloading
https://www.geeksforgeeks.org/c-sharp-method-overloading/
Is the common way of implementing polymorphism. It is the ability to redefine a function in more than one form. A user can implement function overloading by defining tw …
_________
_________
Enumeration types
https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum
Is a value type defined by a set of named constants of the underlying integral numeric type. To define an enumeration type, use the enum keyword and specify the names o …
_________

*/
//Your code should go here:

