#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
# https://leetcode.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (62.08%)
# Likes:    900
# Dislikes: 30
# Total Accepted:    138.7K
# Total Submissions: 223.2K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# We have a collection of stones, each stone has a positive integer weight.
#
# Each turn, we choose the two heaviest stones and smash them together.
# Suppose the stones have weights x and y with x <= y.  The result of this
# smash is:
#
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of
# weight y has new weight y-x.
#
#
# At the end, there is at most 1 stone left.  Return the weight of this stone
# (or 0 if there are no stones left.)
#
#
#
# Example 1:
#
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the
# value of last stone.
#
#
#
# Note:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

      for i, _ in enumerate(stones):
        stones[i] *= -1

      # Heapify is a maxheap. To make it min heap, just reverse the items in list
      heapq.heapify(stones)

      # Smash stones as long as we have two to smash together
      while len(stones) > 1:
        stone_1 = heapq.heappop(stones) # Pop out smallest stone
        stone_2 = heapq.heappop(stones) # Pop out second smallest stone

        if stone_1 != stone_2:
          heapq.heappush(stones, stone_1 - stone_2)

      if len(stones) == 1:
        return -stones[0]
      else:
        return 0

# @lc code=end

