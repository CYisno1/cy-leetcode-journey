
"""
Ex.
nums = [1, 1, 1, 2, 2, 3]
k = 2

count = {1: 3, 2: 2, 3: 3}

heapq.nlargest(n, iterable, key=None)
n: Number of top elements you want to retrieve
iterable: 	A list, dictionary keys, or any iterable to extract the top n elements from
key: (Optional) A function that serves as a custom sort comparator 排序依據
return as a list
"""

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)
