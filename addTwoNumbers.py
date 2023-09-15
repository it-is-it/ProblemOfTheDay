# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize variables to keep track of the carry and the result linked list.
        carry = 0
        dummy_head = ListNode()  # Create a dummy head for the result linked list.
        current = dummy_head  # Initialize a current pointer to the dummy head.

        # Traverse both input linked lists while considering the carry.
        while l1 or l2 or carry:
            # Get the values from the current nodes or set to 0 if the node is None.
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current digits, including the carry.
            total = value1 + value2 + carry
            carry = total // 10  # Calculate the carry for the next iteration.

            # Create a new node with the current digit and append it to the result.
            current.next = ListNode(total % 10)
            current = current.next  # Move the current pointer to the new node.

            # Move to the next nodes in the input lists if they exist.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # The result is stored starting from the node after the dummy head.
        return dummy_head.next

# Helper function to convert a list to a linked list for testing.
def list_to_linked_list(lst):
    dummy_head = ListNode()
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

# Helper function to convert a linked list to a list for testing.
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: 2 -> 4 -> 3 + 5 -> 6 -> 4 = 7 -> 0 -> 8
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]

    # Test case 2: 0 + 0 = 0
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [0]

    # Test case 3: 9999999 + 9999 = 10009998 
    l1 = list_to_linked_list([9,9,9,9,9,9,9])
    l2 = list_to_linked_list([9,9,9,9])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_list(result) == [8,9,9,9,0,0,0,1]

    print("All test cases passed!")
