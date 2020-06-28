#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#
# https://leetcode.com/problems/distribute-candies/description/
#
# algorithms
# Easy (61.25%)
# Likes:    446
# Dislikes: 848
# Total Accepted:    97.8K
# Total Submissions: 159.8K
# Testcase Example:  '[1,1,2,2,3,3]'
#
# Given an integer array with even length, where different numbers in this
# array represent different kinds of candies. Each number means one candy of
# the corresponding kind. You need to distribute these candies equally in
# number to brother and sister. Return the maximum number of kinds of candies
# the sister could gain.
#
# Example 1:
#
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for
# each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has
# candies [1,2,3], too.
# The sister has three different kinds of candies.
#
#
#
# Example 2:
#
# Input: candies = [1,1,2,3]
# Output: 2
# Explanation: For example, the sister has candies [2,3] and the brother has
# candies [1,1].
# The sister has two different kinds of candies, the brother has only one kind
# of candies.
#
#
#
# Note:
#
# The length of the given array is in range [2, 10,000], and will be even.
# The number in given array is in range [-100,000, 100,000].
#
#
#

# @lc code=start

# Notes: The list is of even length, never 0. The numbers can be negative.
# We need to maximize the number of different candies for the sister.
# ie; what is the most unique we can have while still evenly distributing
# the total number of candies amongst two people?

# It's interesting to take note of the total unique candies. That'd be a good place to start
# How to do that? we can make a set and then count the unique.
# Given the list, we also have an interesting number: the total number of candies to divide.
# So we have:
# 1. total unique candies count
# 2. total num of candies to disperse
# So if unique candies count > half-of-total-num-candies, we know the sister cannot have
# at least one of every single kind of candy, bc otherwise she would have more than half
# of the total candy. SO the maximum she can have is up to the half the total num of candies.
#
# Conversely, if the total num of unique candies is less than the half of the total num of candies,
# we know that she must then must have at least one of each unique candy to maximize.
from typing import List
class Solution:
  def distributeCandies(self, candies: List[int]) -> int:
    unique_candies = set(candies)
    unique_candy_count = len(unique_candies)

    if unique_candy_count <= len(candies) // 2:
      return unique_candy_count
    else:
      return len(candies) // 2


# @lc code=end

print(Solution().distributeCandies([1,1,2,2,3,3]))