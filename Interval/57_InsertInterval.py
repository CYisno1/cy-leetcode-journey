"""
We use Binary Search to find where to insert the newInterval. First, we compare the start of the middle interval with the first element of the new intrval, which we name it as target.
If the start of mid interval is less than the target, update left to mid + 1 to search the right half of the search space. Otherwise, update right to mid - 1 to search the left half of the search space.
We then insert the newInterval, and then we have to merge it correctly with the original intervals.
If the end of the result interval is smaller than the end of the new interval, directly insert the new interval; don't need to merge.
Else, if the end of the new interval bigger than the res one, choose the bigger one as the final end.
"""

class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]
    
        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 1
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)
        
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
            
        return res
