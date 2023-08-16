"""
####  Merge Two Sorted Lists  ####

Merge two sorted linked-lists and return it as a new sorted linked-list. The new linked-list should be made by splicing together the nodes of two linked-lists.



[Input]

The class for nodes of the singly-linked list is defined in the Tests tab. The linked-lists are made from the data of ordinary lists and provided into the function. Each node contains a value and the reference to the next node.
___
class ListNode:
    def __init__(self, val=0, next_element=None):
        self.val = val
        self.next_element = next_element
_____



[Output]

Return the reference to the first node of the non-empty sequence of data. If one of the linked lists is None, return reference to another. If both linked lists are None, return None. If both linked lists have data, arrange the references such that a new sorted linked list is formed.


[Examples]

___
a1 = [1, 2, 4]
a2 = [1, 3, 4]
lst1 = ListNode(a1[0]) if a1 else None
if a1 and len(a1) > 1:
    lst1.add_data(a1[1:])
lst2 = ListNode(a2[0]) if a2 else None
if a2 and len(a2) > 1:
    lst2.add_data(a2[1:])
merged_lst = merge_two_lists(lst1, lst2)
print(merged_lst.all_nodes_data() if merged_lst else []) ➞ [1, 1, 2, 3, 4, 4]

b1 = [13, 69]
b2 = []
lst1 = ListNode(b1[0]) if b1 else None
if b1 and len(b1) > 1:
    lst1.add_data(b1[1:])
lst2 = ListNode(b2[0]) if b2 else None
if b2 and len(b2) > 1:
    lst2.add_data(b2[1:])
merged_lst = merge_two_lists(lst1, lst2)
print(merged_lst.all_nodes_data() if merged_lst else []) ➞ [13, 69]

lst1 = None
lst2 = None
merged_lst = merge_two_lists(lst1, lst2)
print(merged_lst.all_nodes_data() if merged_lst else []) ➞ []
_____



[Notes]

Try to avoid making new nodes and copying values (focus on rearranging self.next_element).


[classes] [data_structures] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

