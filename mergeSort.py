# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def merge_sorted_lists(self, l1, l2):
        # Create a dummy node to simplify code
        dummy = ListNode(-1)
        # The current pointer starts at the dummy node
        current = dummy
        
        # Iterate until either of the input lists becomes empty
        while l1 is not None and l2 is not None:
            # Compare the values of the current nodes in l1 and l2
            if l1.value < l2.value:
                # If the value in l1 is smaller, append it to the merged list
                current.next = l1
                # Move l1 pointer to the next node in l1
                l1 = l1.next
            else:
                # If the value in l2 is smaller or equal, append it to the merged list
                current.next = l2
                # Move l2 pointer to the next node in l2
                l2 = l2.next
            # Move the current pointer to the last node in the merged list
            current = current.next
        
        # If one of the input lists is not empty, append the remaining nodes to the merged list
        if l1 is not None:
            current.next = l1
        if l2 is not None:
            current.next = l2
        
        # The merged list starts from the next node of the dummy node
        return dummy.next

# Example usage
solution = Solution()

# Convert input lists to linked list nodes
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge the sorted lists
merged_list = solution.merge_sorted_lists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.value, end=" -> ")
    merged_list = merged_list.next

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 ->