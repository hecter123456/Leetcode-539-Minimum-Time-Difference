import unittest
import sys

class unitest(unittest.TestCase):
    def testSameTime(self):
        Input = ["00:00","00:00"]
        Ans = 0
        self.assertEqual(Solution().findMinDifference(Input),Ans)
    def testCrossHour(self):
        Input = ["23:00","21:20"]
        Ans = 100
        self.assertEqual(Solution().findMinDifference(Input),Ans)
    def testCrossDay(self):
        Input = ["23:59","01:20"]
        Ans = 81
        self.assertEqual(Solution().findMinDifference(Input),Ans)
    def testFourInput(self):
        Input = ["23:59","01:20","23:00","21:20"]
        Ans = 59
        self.assertEqual(Solution().findMinDifference(Input),Ans)

class Solution():
    def findMinDifference(self, timePoints):
        mins = sorted((int(mins[:2]) * 60 + int(mins[3:])) for mins in timePoints)
        mins.append(mins[0]+1440)
        return min(b-a for (a,b) in zip(mins,mins[1:]))

if __name__ == '__main__':
    unittest.main()
