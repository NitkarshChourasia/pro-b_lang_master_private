"""
####  Move the Discs  ####

There are 3 adjacent slots - L, M and R - which can each hold a number of discs. L can hold 3 discs, M can hold 2 and L 3. The total number of discs can vary from 3 to 5, and the discs are numbered 1, 2, 3 and up to 5. From a given configuration of discs, it is possible to move 1 disc at a time provided the disc concerned is top of its slot and there is an available slot in the destination slot.
Write a function which takes 2 parameters (start and end) and returns a tuple (n, moves) where n is the minimum number of moves needed to move from start to end and moves is a list of the moves required to effect the changes. start and end are 8 digit strings where the 1st 3 are slot L, next 2 M and the last 3 R. Locations are shown from bottom to top within each slot, and empty locations are represented by 0s. So configuration '15040230' represents disc 5 above 1 in slot L, 4 in slot M and 3 above 2 in slot R. '45000231' encodes 5 above 4 in slot L, an empty slot M and 1 above 3 above 2 in slot R.
A move is a string in the form <disc>-><slot>. So to move disc 5 to slot M you would write "5->M"; 4 to slot R would be "4->R" and 3 to L "3->L". Slots act like stacks; you can only take the top disc and slots fill up from the bottom up so you can never have a space below a disc.


[Examples]

___
move_discs("15040230", "45000231") -> (6,["4->R","5->M","1->M","4->L","1->R","5->L"])
# "15040230" with "4->R" gives "15000234"
# "15000234" with "5->M" gives "10050234"
# "10050234" with "1->M" gives "00051234"
# "00051234" with "4->L" gives "40051230"
# "40051230" with "1->R" gives "40050231"
# "40050231" with "5->L" gives "45000231"
_____



[Notes]

___
*) Start and end will always be valid configurations - you can deduce the number of discs to move from either.
*) There may be more than 1 minimum sequence of moves. To check this, the Code section contains the validate function. This checks that the minimum number of moves have been made and that each is legal and applying them in sequence leads from start of end. You may find it useful for debugging your code as you develop it.
*) If you are unsure how to proceed, the Resources section may provide some pointers.
___



[algorithms] [data_structures] [games] 



-------------------------------------------------------------------
[Resources]
_________
Graph Data Structure And Algorithms
https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/#:~:text=A%20Graph%20is%20a%20non,Graph%20can%20be%20defined%20as%2C&text=For%20example%2C%20in%20Facebook%2C%20each,a%20vertex(or%20node).
A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect …
_________
_________
Breadth First Search
https://en.wikipedia.org/wiki/Breadth-first_search
Is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'se …
_________

"""
#Your code should go here:

