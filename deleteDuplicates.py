# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                # Duplicate found, skip the next node
                current_node.next = current_node.next.next
            else:
                # Move to the next node
                current_node = current_node.next

        return head

# Example 2 usage:
values = [1, 1, 2, 3, 3]
linked_list = ListNode(values[0])
current_node = linked_list
for value in values[1:]:
    current_node.next = ListNode(value)
    current_node = current_node.next

solution = Solution()
result_head = solution.deleteDuplicates(linked_list)

# Printing the result
current_node = result_head
while current_node:
    print(current_node.val, end=" ")
    current_node = current_node.next
