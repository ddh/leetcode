"""
https://leetcode.com/problems/high-five/

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.



Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.



Note:

    1 <= items.length <= 1000
    items[i].length == 2
    The IDs of the students is between 1 to 1000
    The score of the students is between 1 to 100
    For each student, there are at least 5 scores

"""

from typing import List
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

      # O(nlogn) for sorting by student id + score. The trick to sort by score by descending is to flip the sign.
      items.sort(key=lambda student: (student[0], student[1] * -1))

      answer = []

      for i, student in enumerate(items):
        student_id = items[i][0]
        if i == 0 or student_id != items[i - 1][0]:
          answer.append([student_id, sum(v for k, v in items[i:i+5])//5])

      return answer


# Driver:
print(Solution().highFive([[2,77],[1,91],[1,92],[2,93],[2,97],[1,60],[1,65],[1,87],[1,100],[2,100],[2,76]])) # [[1,87],[2,88]]