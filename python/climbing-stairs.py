"""
https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


"""

# Idea: Recognize that this is fibonacci. Answer is the nth fib number.
# Idea2: Another way you can do this is memoization

class Solution:
    def climbStairs(self, n: int) -> int:

      # Base case:
      if n == 1:
        return 1

      first = 1
      second = 2

      ith = 3

      while ith <= n:
        first, second = second, first + second
        ith += 1

      # print(second)
      return second

# Brute force, recursion. It is naiive approach because we're repeating a lot of work during the recursion.
# Time limited execeeded because at each step, we have two choices: take one step, or take two step.
# Then at most, we're taking n steps (each step being 1). In each step, we can either take one or two.
# So that works out to O(2^n), which isn't so hot.
class Solution2:
    def climbStairs(self, n: int) -> int:
      self.steps = n

      def climb(step):
        # Here, we finished climbing and got to the top. So we return '1' to indicate one more way to get to the top.
        if step == self.steps:
          return 1

        # If the step we're on is greater than the max steps, we return 0 to indicate it is not a valid way.
        if step > self.steps:
          return 0

        # Here, we climb either one steps, or two steps
        return climb(step + 1) + climb(step + 2)

      return climb(0)

# Similar to the brute force but instead, we save us some work and memoize.
class Solution3:
    def climbStairs(self, n: int) -> int:
      self.steps = n
      self.memo = [None] * (n + 1) # We have to plus one because the 0th element is no steps.

      def climb(step):

        # if there is something in memo, return it so we don't have to do the work again!
        if step <= self.steps and self.memo[step]:
          return self.memo[step]

        # Here, we finished climbing and got to the top. So we return '1' to indicate one more way to get to the top.
        if step == self.steps:
          return 1

        # If the step we're on is greater than the max steps, we return 0 to indicate it is not a valid way.
        if step > self.steps:
          return 0

        # Here, we climb either one steps, or two steps. This will do the work of filling out the memo.
        self.memo[step] = climb(step + 1) + climb(step + 2)

        # Then in the end, we just return
        return self.memo[step]

      return climb(0)




# Driver:
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))

print(Solution2().climbStairs(2))
print(Solution2().climbStairs(3))
print(Solution2().climbStairs(4))
print(Solution2().climbStairs(5))

print(Solution3().climbStairs(2))
print(Solution3().climbStairs(3))
print(Solution3().climbStairs(4))
print(Solution3().climbStairs(5))