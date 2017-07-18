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
        def GetTotal(timePointsA,timePointsB):
            if(timePointsA == timePointsB):
                return 0
            hour = int(timePointsA[:2]) - int(timePointsB[:2])
            minute = int(timePointsA[3:]) - int(timePointsB[3:])
            total = abs(hour*60 + minute)
            total = min(total,abs(total-1440))
            return total
        timePoints.sort(key = lambda a : (int(a[:2]),int(a[3:])))
        Ans = sys.maxsize
        for indexA in range(len(timePoints)-1):
            Ans = min(Ans,GetTotal(timePoints[indexA],timePoints[indexA+1]))
        Ans = min(Ans,GetTotal(timePoints[0],timePoints[len(timePoints)-1]))
        return Ans
        

if __name__ == '__main__':
    unittest.main()
