
"""
Ex.
nums = [1, 1, 1, 2, 2, 3]
k = 2

count = {1: 3, 2: 2, 3: 1}

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



"""
250818

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for key, val in counter.items():    # key is the number, val is the frequency
            heapq.heappush(heap, (-val, key)) # bc of min-heap, the val has to be negative; heaptify the number and frequency as tuples
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1]) # #bc of the negative value, we will pop out the k-most frequent numbers, nd add the key([1]) to the res
        
        return res

"""
