"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

      # Flip the sign, so the list will work in a min-heap
      # But be sure to flip the sign back when done
      for i, stone in enumerate(stones):
        stones[i] *= -1

      # Heap structure, where the min is the top.
      heapq.heapify(stones) # Heapify in-place

      # As long as we have 2 or more stones, we smash stones together.
      while len(stones) > 1:
        stone_1 = heapq.heappop(stones)
        stone_2 = heapq.heappop(stones)

        # If the stones are not equal, the remaining difference is put back into the heap
        if stone_1 != stone_2:
          heapq.heappush(stones, stone_1 - stone_2)

      # Flip the sign and return the result. Either the last stone or no stones.
      return -stones[0] if stones else 0

# Driver
print(Solution().lastStoneWeight([2,7,4,1,8,1])) # 1