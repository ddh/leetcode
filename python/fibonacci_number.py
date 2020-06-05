"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.



Note:

0 ≤ N ≤ 30.
"""

# Naive Recursive solution. It is slow O(2^n)
class Solution:
    def fib(self, N: int) -> int:
        if N == 1 or N == 2:
          return 1
        else:
          return self.fib(N-1) + self.fib(N-2)

# Saving the intermediate steps; memoization.
class Solution2:
    def fib(self, N: int) -> int:

      # Base case 0:
      if N == 0:
        return 0

      # We have to offset the array so when we want the 1st fib number, we're talking about index 1, not 0
      self.cached_results = [None] * (N + 1)

      # Helper function to use the cached results
      def fib_using_cache(self, n):

        # If we already have the cached answer, return it!
        if self.cached_results[n]:
          return self.cached_results[n]

        # Base cases; 1st and 2nd always 1.
        if n == 1 or n == 2:
          result = 1
        # As for the rest, nth fibonacci == the sum of previous two fibonaccis
        else:
          result = fib_using_cache(self, n - 1) + fib_using_cache(self, n - 2)

        # Save the answer to be used for later calculations when it comes up
        self.cached_results[n] = result

        return result

      return fib_using_cache(self, N)

# Idea: Attempt to do bottom-up approach by building the array of results as we go.
class Solution3:
  def fib(self, N: int) -> int:

    # Base case:
    if N == 0:
      return 0

    # Base case:
    if N == 1 or N == 2:
      return 1

    cached_results = [None] * (N+1) # Ready the array
    cached_results[1], cached_results[2] = 1, 1 # Prime the first two in sequence

    # Iterate through the rest of the array
    for i in range(N+1):
      if i == 0 or i == 1 or i == 2:
        continue
      cached_results[i] = cached_results[i-1] + cached_results[i-2]

    return cached_results[N]

# Idea: Attempt another bottom-up solution but this time, updating a pair of variables that will hold our last two results
class Solution4:
  def fib(self, N: int) -> int:

    # Base Case:
    if N == 0:
      return 0

    # Base Cases:
    if N == 1 or N == 2:
      return 1

    prev_prev_result = 1
    prev_result = 1

    # We want to iterate N-2 times
    for _ in range(N-2):
      prev_prev_result, prev_result = prev_result, prev_prev_result + prev_result

    return prev_result

print(Solution().fib(8))
print(Solution2().fib(8))
print(Solution3().fib(8))
print(Solution4().fib(8))