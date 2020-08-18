#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/
#
# algorithms
# Easy (78.72%)
# Likes:    180
# Dislikes: 48
# Total Accepted:    34.7K
# Total Submissions: 44.5K
# Testcase Example:  '[1,2,3]\n[3,2,7]\n4'
#
# Given two integer arrays startTime and endTime and given an integer
# queryTime.
#
# The ith student started doing their homework at the time startTime[i] and
# finished it at time endTime[i].
#
# Return the number of students doing their homework at time queryTime. More
# formally, return the number of students where queryTime lays in the interval
# [startTime[i], endTime[i]] inclusive.
#
#
# Example 1:
#
#
# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and
# wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2
# and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and
# was the only student doing homework at time 4.
#
#
# Example 2:
#
#
# Input: startTime = [4], endTime = [4], queryTime = 4
# Output: 1
# Explanation: The only student was doing their homework at the queryTime.
#
#
# Example 3:
#
#
# Input: startTime = [4], endTime = [4], queryTime = 5
# Output: 0
#
#
# Example 4:
#
#
# Input: startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
# Output: 0
#
#
# Example 5:
#
#
# Input: startTime = [9,8,7,6,5,4,3,2,1], endTime =
# [10,10,10,10,10,10,10,10,10], queryTime = 5
# Output: 5
#
#
#
# Constraints:
#
#
# startTime.length == endTime.length
# 1 <= startTime.length <= 100
# 1 <= startTime[i] <= endTime[i] <= 1000
# 1 <= queryTime <= 1000
#
#
#

# @lc code=start

from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        pointer = 0
        students_count = len(startTime)
        answer = 0
        for _ in range(students_count):
          if startTime[pointer] <= queryTime <= endTime[pointer]:
            answer += 1
          pointer += 1
        return answer
# @lc code=end

print(Solution().busyStudent([1,2,3], [3,2,7], 4))