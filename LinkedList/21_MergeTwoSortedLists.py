class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prehead = ListNode(-1) # Initialize a dummy node (not in the actual Linked List)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val: 
                prev.next = l1 # Add the node to the answer list
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next # Move the prev forward so that the added node from l1 or l2 will be linked to the correct place (讓 prev 也往後移，否則下一次會把新節點接在舊位置後面)
        
        prev.next = l1 if l1 is not None else l2 # Add the nodes left (whether they are from l1 or l2)

        return prehead.next
