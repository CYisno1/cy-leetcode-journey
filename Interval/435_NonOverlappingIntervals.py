"""
Ex. [[1,2],[2,3],[3,4],[1,3]]
Sort the intervals according to their ends. >> [[1,2],[2,3],[1,3],[3,4]]
Initialize prev to represent the first interval, and count to represent the intervals which are not overlapping.
Check whether the start of the next interval is larger than or equal to the end of the previous interval; if it is, they are not ovrlapped.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) 
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1
        
        return n - count
