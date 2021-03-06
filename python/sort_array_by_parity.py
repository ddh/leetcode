"""
905. Sort Array By Parity
Easy

880

71

Add to List

Share
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = [num for num in A if num % 2 == 0 ]
        odd = [num for num in A if num % 2 == 1]
        return even + odd


# Driver:
print(Solution().sortArrayByParity([3,1,2,4])) # [2,4,3,1]