"""
####  Functions with goto Logic  ####

Python language does not have goto keyword. In other languages such statements exist. For example in C++: the goto statement transfers control to the location specified by label. The goto statement must be in the same function as the label it is referring, it may appear before or after the label.
One good use of goto is to exit from a deeply nested routine. For example, consider the following code fragment:
___
for(...) {
   for(...) {
      while(...) {
         if(...)
             goto stop;
      }
   }
}
stop:
_____

Use of goto statement is highly discouraged because it makes it difficult to trace the control flow of a program, making the program hard to understand and hard to modify. Any program that uses a goto can be rewritten so that it doesn't need the goto.
The above point of view is not being disputed. This here is just a challenge to amuse your imagination: how to translate a function with goto into a function without goto.


[Goal]

Write a function that can translate the given function source code into a proper function that can execute according to the goto instructions.


[Input]

The translation function receives a multiline Python source code string of an intended function with goto and labels statements. These additional instructions are, technically comments, formatted in the following manner:
___
# goto label_name;
...
# label_name:
_____



[Output]

The Python functions can make other functions. To accomplish the goal, you need to know how to make a runnable function from the text and how to improve the given text such that the output function jumps to the label whenever it encounters a goto statement.


[Examples]

The intended function receives a list and two numbers. It has to select sub_len first elements from the list n_subs times and output a new list. The make_fun function processes the source code and returns a function that handles the goto jumps.
___
str_code = """
def make_list(lst, sub_len, n_subs):
    res = []
    sub_count = 0
    # label1:
    for i, val in enumerate(lst):
        if sub_count < n_subs:
            if i < sub_len:
                res.append(val)
            elif i >= sub_len:
                sub_count += 1
                # goto label1;
        else:
            pass
            # goto label2;
    # label2:
    return res
"""

lst = ["g", "o", 2, ":", 8, "t", "a", "i", "l"]

f = make_fun(str_code)

f(lst, 5, 4) ➞ ["g", "o", 2, ":", 8, "g", "o", 2, ":", 8, "g", "o", 2, ":", 8, "g", "o", 2, ":", 8]

f(lst, 2, 3) ➞ ["g", "o", "g", "o", "g", "o"]

f(lst, 8, 2) ➞ ["g", "o", 2, ":", 8, "t", "a", "i", "g", "o", 2, ":", 8, "t", "a", "i"]
_____



[Notes]

Performance is not a concern. There are no heavy computations in the tests. Everything runs under 0.01 seconds. The focus of this challenge is on string manipulation and the goto jump’s logic.


[logic] [strings] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

