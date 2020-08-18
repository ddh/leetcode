#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (32.99%)
# Likes:    710
# Dislikes: 803
# Total Accepted:    64.7K
# Total Submissions: 195.6K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
#
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
#
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
#
# Note:
#
#
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
#
#
#
#
# Example 2:
#
#
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
#
#
#
#
#

# @lc code=start
from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        current_count = 0
        heaters = set(heaters)
        houses.sort()
        distances = []

        # Iterate through once, keeping count of the distances in between heaters
        for house in houses:
          if house in heaters:
            distances.append(current_count)
            current_count = 0
          else:
            current_count += 1

        # Record remaining distances if last house was not a heater
        if current_count > 0: distances.append(current_count)

        return -(-max(distances)//2)
# @lc code=end

print(Solution().findRadius([1,2,3,4,5,6], [1,4]))
print(Solution().findRadius([1,3,2,4,5,6,7,8,9,10,11,12,13], [3,7,12]))