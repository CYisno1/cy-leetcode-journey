"""
Use two pointers!

head = 1 → 2 → 3 → 4 → 5
n = 2

(for loop: move first node first so that the gap between first and second is n nodes apart)
D → 1 → 2 → 3 → 4 → 5
    h       f

(while loop: let second follow the first, and move to the node before the node we want to delete)
D → 1 → 2 → 3 → 4 → 5
    h       s          f (first moves to the end)

After second.next = second.next.next
D → 1 → 2 → 3 → 5
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
