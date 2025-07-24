from heapq import heappush, heappop

class MedianFinder:

  # Initialize the object
    def __init__(self):
        self.lo = []     # The maxheap to store the smaller half of the number
        self.hi = []     # The minheap to store the larger half of the number
    
    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)                   # Push the -num into lo maxheap
        heappush(self.hi, -self.lo[0])            # Add the -self.lo[0] (which will be positive and at the top of hi) into hi min heap
        heappop(self.lo)

      # If two heaps are not balance (because we want the len(low) >= len(high))
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)
        
    def findMedian(self) -> float:
      # If lo has more elements, the median is the top of lo
        if len(self.lo) > len(self.hi):
            return -self.lo[0]

      # If both heaps are equal in size, median is the average of the two middle values
        return (-self.lo[0] + self.hi[0]) / 2
