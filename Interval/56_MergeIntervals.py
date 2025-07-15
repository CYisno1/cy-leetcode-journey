class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # Sort by start
        merged = []
        prev = intervals[0] # First interval in intervals = prev

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]: #Overlap
                prev[1] = max(prev[1], intervals[i][1])
            else:
                merged.append(prev)
                prev = intervals[i]
        
        merged.append(prev)
        return merged
