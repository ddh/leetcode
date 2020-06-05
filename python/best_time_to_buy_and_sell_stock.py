"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

# Brute force would have you making all sorts of combinations then finding the largest profit.

# Idea: Let's keep track of the min number and the max profit as we iterate through the array once
# We'll only have to iterate once through the array
# Another way to look at this is to find the min valley then the max peak that occurs after the min

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

      # Base case
      if not prices:
        return 0

      min_purchase = prices[0]
      max_profits = 0

      for price in prices:
        # Record the smallest purchase price so far
        min_purchase = min(min_purchase, price)
        # Record the largest profits so far
        max_profits = max(max_profits, price - min_purchase)

      return max_profits





# Driver:
print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0