"""
####  Regroup the Linked List  ####

The function is given a linked list node1->node2->node3->node4->node5->None. Relink the original list such that first all odd nodes and then all even nodes follow each other preserving the original order of appearance. The changed list should be: node1->node3->node5->node2->node4->None. The Linked List Class is defined in the Tests tab:
___
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
_____

The class has .val field and reference for the next node .next. The function receives the reference to the list head, rearranges the internal links and returns the reference to the head.


[Examples]

___
lst = [12, 21]
ll = ListNode(lst[0])
ll.add_data(lst[1:])
odd_even_list(ll).get_data() ➞ [12, 21]

lst = [8, 7, 6]
ll = ListNode(lst[0])
ll.add_data(lst[1:])
odd_even_list(ll).get_data() ➞ [8, 6, 7]

lst = [1, 2, 3, 4, 5, 6]
ll = ListNode(lst[0])
ll.add_data(lst[1:])
odd_even_list(ll).get_data() ➞ [1, 3, 5, 2, 4, 6]
_____



[Notes]

It is preferable to relink the list in place, without making new nodes, although other less efficient solutions can also pass.


[algorithms] [classes] [control_flow] [data_structures] 



-------------------------------------------------------------------
[Resources]
_________
Singly Linked Lists
https://www.codesdope.com/course/data-structures-linked-lists/
Learn the concepts of singly linked list and code it in C, Java and Python. Learn about nodes and its connections.
_________

"""
#Your code should go here:

