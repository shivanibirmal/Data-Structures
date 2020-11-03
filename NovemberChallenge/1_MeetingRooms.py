# 252. Meeting Rooms
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: true
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals.length == 2
# 0 <= starti < endi <= 106
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        sorted_list = sorted(intervals, key = lambda x : x[0])

        for i in range(len(sorted_list)):
            if i < len(sorted_list)-1:
                if not(sorted_list[i+1][0] >= sorted_list[i][1]):
                    return False

        return True

obj = Solution()
intervals = [[0,30],[5,10],[15,20]]
print("Meeting intervals:", intervals)
result = obj.canAttendMeetings(intervals)
if result == True:
    print("Can attend meetings ? Yes")
else:
    print("Can attend meetings ? No")





