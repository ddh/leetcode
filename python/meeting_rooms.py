"""
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

# Idea: We can sort each meeting by its start time. Then we can iterate to make sure
# the ending time is less than the start time of the next array
# Sorting takes O(nlogn) and we're using the same array for answer, so O(1) space

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
      intervals.sort(key=lambda meeting: meeting[0])
      for i, meeting in enumerate(intervals[:-1]):
        if meeting[1] > intervals[i+1][0]:
          return False
      return True


# Driver:
print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]])) # false
print(Solution().canAttendMeetings([[7,10],[2,4]])) # True