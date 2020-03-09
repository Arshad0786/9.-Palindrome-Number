import unittest
from PalindromeNumber import Solution


class ReverseIntegerTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.value = 121 
        self.assertEqual(temp.isPalindrome(self.value), True) 
    

if __name__ == "__main__":
    unittest.main()
