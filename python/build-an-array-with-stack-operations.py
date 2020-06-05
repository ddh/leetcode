"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

    Push: Read a new element from the beginning list, and push it in the array.
    Pop: delete the last element of the array.
    If the target array is already built, stop reading more elements.

You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.



Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation:
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]

Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.

Example 4:

Input: target = [2,3,4], n = 4
Output: ["Push","Pop","Push","Push","Push"]



Constraints:

    1 <= target.length <= 100
    1 <= target[i] <= 100
    1 <= n <= 100
    target is strictly increasing.


"""

# Idea: We need to create the target array, given a list of numbers 1,2,3...n.
# We know that the array is strictly increasing, since we push 1, then 2, and so on.
# For any number not in the target array, we want to pop it out.
# Numbers in target only contain 1 to n. Numbers are unique

from typing import List
from collections import deque
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

      # Base cases:
      # if n == 0 or len(target) is None:
      #   return ['']

      # Create our list of 'n' numbers:
      list = deque([num + 1 for num in range(n)])


      # Define push action
      def push(value):
        # print(f'Pushed: {value}') # Debug
        self.operations.append("Push")
        self.stack.append(value)

      # Define the pop action:
      def pop():
        # print(f'Popped: {self.stack[-1]}') # Debug
        self.operations.append("Pop")
        return self.stack.pop()

      # Instantiate the stack:
      self.stack = []
      self.operations = []
      target_pointer = 0

      while target_pointer <= len(target) - 1:
        push(list.popleft())
        if self.stack[-1] != target[target_pointer]:
          pop()
        else:
          target_pointer += 1

      return self.operations

# Driver
print(Solution().buildArray([1,3], 3)) # ["Push","Push","Pop","Push"]
# print(Solution().buildArray([1,2,3], 3)) # ["Push","Push","Pop","Push"]
print(Solution().buildArray([2,3,4], 4)) # ["Push","Pop","Push","Push","Push"]
