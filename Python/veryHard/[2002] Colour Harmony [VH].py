"""
####  Colour Harmony  ####

In colour theory, colour harmony refers to an aesthetically pleasing combination of colours. The standard colour wheel shows the 12 primary, secondary and tertiary colours. Starting with red, and moving clockwise, the colours are:
___
colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
_____

With an initial colour (called the anchor), you can find combinations of harmonious colours. The combination types are shown below, for an anchor colour of green:

Given an anchor colour and a combination type, write a function that returns a set containing all colours within the combination.


[Examples]

___
colour_harmony("green", "triadic") ➞ { "green", "violet", "orange" }

colour_harmony("blue-green", "complementary") ➞ { "blue-green", "red-orange" }

colour_harmony("orange", "analogous") ➞ { "yellow-orange", "red-orange", "orange" }
_____



[Notes]

___
*) Create the combinations given their relative positions from the anchor colour. For example, the rectangle combination starts with the colours two positions clockwise and four positions anti-clockwise from the anchor (and not the other way around). With the split-complemetary combination, you take the colours five positions both clockwise and anti-clockwise from the anchor. For the analogous combination, you include the colours directly on either side of the anchor.
*) Include the anchor colour in the final set.
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Colour Combinations
http://www.tigercolor.com/color-lab/color-theory/color-harmonies.htm
Further detail on colour combination "chords".
_________
_________
Basic Colour Theory Explained
https://www.colormatters.com/color-and-design/basic-color-theory
Color theory encompasses a multitude of definitions, concepts and design applications - enough to fill several encyclopedias. However, there are three basic categories …
_________

"""
#Your code should go here:

