"""
Given an integer n, return any array containing n unique integers such that they add up to 0.



Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]

Example 3:

Input: n = 1
Output: [0]



Constraints:

    1 <= n <= 1000

"""

# Idea: This one looks easy. If we're trying to add n unique integers that add up to 0,
# what we can do is add a positive number with its corresponding negative number.
# If n is even, we just iterate from 1 and pair each number with its negative.
# If n is odd, we just tack on a 0 since nothing says we can't use that as part of the answer.

from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:

      uniq_nums = []

      if n % 2 == 1:
        uniq_nums.append(0)
      for i in range(n//2):
        uniq_nums.append(i+1)
        uniq_nums.append(-(i+1))
      return uniq_nums

# Driver:
print(Solution().sumZero(5)) # [-7,-1,1,3,4]
print(Solution().sumZero(3)) # [-1,0,1]
print(Solution().sumZero(1)) # [0]