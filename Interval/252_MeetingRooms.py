"""
First sort the intervals and check if the end of the current interval is larger than the start of the next interval, which means they are overlapped.
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
            
        return True
