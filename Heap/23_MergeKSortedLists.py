import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        heap = []

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node)) # Have both node.val and i to prevent messing up the nodes with same value
        
        dummy = ListNode(-1)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap) # take out node and 
            curr.next = node                   # link it to the result list
            curr = curr.next
            if curr.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next


        

        
