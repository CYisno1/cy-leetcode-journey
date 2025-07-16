"""
Ex. lists = [[1 → 4 → 5], [1 → 3 → 4], [2 → 6]]

heapq.heappush(heap, (node.val, i, node)) # Put the i-th list in the heap in the form of tuple
(node.val, i, node) means: (start from the first node (value) in each list, index, the i-th list in lists)
heap = [
    (1, 0, node1a),  # 1st list: 1 → 4 → 5
    (1, 1, node2a),  # 2nd list: 1 → 3 → 4
    (2, 2, node3a)   # 3rd list: 2 → 6
]
Enter the while loop: process the smallest node in the heap one by one

First iteration:
heapq.heappop() → (1, 0, node1a) (the node with value 1 from the first list)
Attach node1a to the result list
curr.next = node1a

Move the pointer forward
curr = curr.next
node1a.next is node1b (which has value 4)

So we need to push the next node from the same list into the heap:
if node.next:
    heapq.heappush(heap, (node.next.val, i, node.next))
This adds (4, 0, node1b) into the heap
"""
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(-1)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if curr.next:
                heapq.heappush(heap, (node.next.val, i, node.next))      

        return dummy.next
