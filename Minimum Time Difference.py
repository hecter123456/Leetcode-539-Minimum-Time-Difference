import unittest

class unitest(unittest.TestCase):
    def testSameTime(self):
        Input = ["00:00","00:00"]
        Ans = 0
        self.assertEqual(Solution().findMinDifference(Input),Ans);

class Solution():
    def findMinDifference(self, timePoints):
        if(timePoints[0] == timePoints[1]):
            return 0

if __name__ == '__main__':
    unittest.main()
