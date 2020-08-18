#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.31%)
# Likes:    628
# Dislikes: 1658
# Total Accepted:    224.1K
# Total Submissions: 408.4K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
#
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
#
# Example:
#
#
# Input: 4
# Output: false
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be
# removed by your friend.
#

# Idea: If there is one stone, you win since you pick first. If there are two stones, you can remove 2. 3, you remove 3.
# Now when there's 4 stones, you can remove up to 3, but that leaves your opponent with the last stone and they win.
# If you remove 2, then they'll remove 2 and win. If you remove just one, they can remove 3 and win.
# So it looks like it boils down to if there's a multiple of 4 stones, you will lose.

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
      return n % 4 != 0

# @lc code=end

