#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (51.40%)
# Likes:    906
# Dislikes: 77
# Total Accepted:    57.5K
# Total Submissions: 111.4K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
#
# You are given n pairs of numbers. In every pair, the first number is always
# smaller than the second number.
#
#
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b
# < c. Chain of pairs can be formed in this fashion.
#
#
#
# Given a set of pairs, find the length longest chain which can be formed. You
# needn't use up all the given pairs. You can select pairs in any order.
#
#
#
# Example 1:
#
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
#
#
#
# Note:
#
# The number of given pairs will be in the range [1, 1000].
#
#
#

# @lc code=start
from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # BC: 0 pairs
        if not pairs:
          return 0

        # BC: 1 pairs
        if len(pairs) == 1:
          return 1

        answer = []

        # First sort the pairs by their SECOND number
        # This is O(nlogn) time complexity
        # This is the trick, to sort by the second number
        # since it has more influence over what you can pick?
        pairs.sort(key=lambda pair: [pair[1]])

        # Iterate through each pair, greedily adding to the answers array
        # We add a pair to the answer if the pair satisfies the rules where the first
        # number of the pair needs to be greater than the last number of the prev pair.
        # Since we have already sorted earlier, we can ensure the numbers at the very least
        # are increasing in reference to the first number.
        # However, what about the second number in the pair? There may be a one to many
        # pairs in a row that will have the same first number but a different second number.
        # In this case, we will need to only add the pair to the answers array if the next pair
        # that we are checking does NOT have the same first number as the current pair we are
        # withholding. We also replace the current pair we are holding if we find that the
        # new pair we are looking at has a smaller second number. The reason we want
        # a smaller second number is because it will give us a better chance (greedily) of
        # the next pair having a smaller first number, which is good in the long run.
        current_pair = None
        for i, pair in enumerate(pairs):
          print(pair)
          if not answer:
            answer.append(pair)
          else:
            # if current pair has the same first num as the last in answers,
            # check to see if the current pair would be a better choice and
            # swap with the last element if it was.
            last_pair = answer[-1]
            if pair[0] == last_pair[0]:
              if pair[1] < last_pair[1]:
                answer[-1] = pair
            else:
              # we need to check if the pair we're currently looking at
              # is at least larger than the last pair we've inserted
              if pair[0] > last_pair[1]:
                answer.append(pair)


        # Bam, we got the answers which is the length of the answers array
        return len(answer)

# @lc code=end

print(Solution().findLongestChain([[1,2],[2,3],[3,4]]))
print(Solution().findLongestChain([[1,8],[1,2],[3,5],[3,4],[4,6],[9,11],[8,12]]))
print(Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
))