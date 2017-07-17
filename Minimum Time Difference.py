import unittest

class unitest(unittest.TestCase):
    def testSameTime(self):
        Input = ["00:00","00:00"]
        Ans = 0
        self.assertEqual(Solution().findMinDifference(Input),Ans);
    def testCrossHour(self):
        Input = ["23:00","21:20"]
        Ans = 100
        self.assertEqual(Solution().findMinDifference(Input),Ans);
    def testCrossDay(self):
        Input = ["23:59","01:20"]
        Ans = 81
        self.assertEqual(Solution().findMinDifference(Input),Ans);

class Solution():
    def findMinDifference(self, timePoints):
        if(timePoints[0] == timePoints[1]):
            return 0
        hour = int(timePoints[0][:2]) - int(timePoints[1][:2])
        minute = int(timePoints[0][3:]) - int(timePoints[1][3:])
        total = abs(hour*60 + minute)
        total = min(total,abs(total-1440))
        return total

if __name__ == '__main__':
    unittest.main()
