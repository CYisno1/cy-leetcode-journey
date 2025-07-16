"""
Ex. Original: head -> 1 -> 2 -> 3 -> 4 -> 5 -> None

After going through the while loop for the 1st time:
1 -> None
prev = 1
curr = 2 -> 3 -> 4 -> 5

2nd time:
next_temp = 3
curr.next = 1    # 2 -> 1
prev = 2
curr = 3

2 -> 1 -> None
prev = 2
curr = 3 -> 4 -> 5
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next # Store the next node or the link will break
            curr.next = prev # Make the current node point to the previous node (change the direction)
            prev = curr # Move the prev forward (prev - curr - next這三個一組的往下一個數字推)
            curr = next_temp
        
        return prev # Now prev is the new head after reverse
