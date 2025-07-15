class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # initialize a min heap to store the end times of the meetings
        free_rooms = []

        # Sort the meetings in increasing order by their starting time
        intervals.sort(key= lambda x: x[0])

        # Add the end time of the first meeting to the heap
        heapq.heappush(free_rooms, intervals[0][1])

        # Check from the second meeting
        for i in intervals[1:]:
            # if the first meeting (free_rooms[0]) ends earlier than the following meeting starts (i[0])
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms) # Assign this room to this meeting
            
            heapq.heappush(free_rooms, i[1]) # Record the end time of this meeting

        return len(free_rooms) # The size of the heap tells us the minimum rooms required for all the meetings.
