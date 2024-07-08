# 160. Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):
# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # If either head is None, there can't be an intersection
        if not headA or not headB:
            return None
        
        # Initialize two pointers to traverse the lists
        currA, currB = headA, headB
        
        # Traverse both lists until the pointers meet or both become None
        while currA != currB:
            # If currA reaches the end of its list, switch to the head of the other list
            # Otherwise, move to the next node
            currA = currA.next if currA else headB
            
            # If currB reaches the end of its list, switch to the head of the other list
            # Otherwise, move to the next node
            currB = currB.next if currB else headA
        
        # When currA == currB, either they have met at the intersection node,
        # or both are None, meaning no intersection
        return currA  # This will be the intersection node or None
    
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Create two linked lists that intersect
listA = create_linked_list([1, 3, 5])
listB = create_linked_list([2, 4])
intersection = create_linked_list([7, 9])

# Attach the intersection part to both lists
currentA = listA
while currentA.next:
    currentA = currentA.next
currentA.next = intersection

currentB = listB
while currentB.next:
    currentB = currentB.next
currentB.next = intersection

# Print the linked lists
print("List A:")
print_linked_list(listA)
print("List B:")
print_linked_list(listB)

# Find the intersection node
solution = Solution()
intersection_node = solution.getIntersectionNode(listA, listB)
print("Intersection at node with value:", intersection_node.val if intersection_node else "No intersection")