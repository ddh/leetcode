class Solution:
    def romanToInt(self, s: str) -> int:
      legend = { 'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000 }
      reversed_string = s.lower()[::-1]
      sum = legend[reversed_string[0]]
      for i, digit in enumerate(reversed_string[:-1]):
        if legend[digit] > legend[reversed_string[i+1]]:
          sum -= legend[reversed_string[i+1]]
        else:
          sum += legend[reversed_string[i+1]]
      return sum

Solution().romanToInt('III')
Solution().romanToInt('IV')
Solution().romanToInt('LVIII') +1+1+1+5+50



