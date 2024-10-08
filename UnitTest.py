from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'s': '][][', 'output': 1},
            2: {'s': "]]][[[", 'output': 2},
            3: {'s': '[]', 'output': 0}
        }
        self.__obj = Solution()
        
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, output = self.__testCases[1].values()
        result = self.__obj.minSwaps(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.__testCases[2].values()
        result = self.__obj.minSwaps(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        s, output = self.__testCases[3].values()
        result = self.__obj.minSwaps(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()