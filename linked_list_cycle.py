# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Import the Optional type hint from the typing module
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, both starting at the head of the linked list.
        slow = head
        fast = head
        
        # Traverse the linked list using the Floyd's Tortoise and Hare algorithm.
        while slow and fast and fast.next:
            # Move the slow pointer one step at a time.
            slow = slow.next
            
            # Move the fast pointer two steps at a time.
            fast = fast.next.next
            
            # If the slow and fast pointers meet at the same node, there is a cycle.
            if slow == fast:
                return True
        
        # If the loop terminates without meeting, there is no cycle in the linked list.
        return False

# Test the hasCycle function with an example linked list.
if __name__ == "__main__":
    # Create nodes for a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (cycle back to 2)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # Create a cycle by pointing the last node back to the second node.
    node5.next = node2
    
    # Initialize the Solution class
    solution = Solution()
    
    # Check for a cycle in the linked list
    has_cycle = solution.hasCycle(node1)
    
    if has_cycle:
        print("The linked list has a cycle.")
    else:
        print("The linked list does not have a cycle.")
