import unittest
from PalindromeNumber import Solution


class ReverseIntegerTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.value = 121
        self.assertEqual(temp.isPalindrome(self.value), True)

    def test_only_two_digits(self):
        temp = Solution()
        self.value = 11
        self.assertEqual(temp.isPalindrome(self.value), True)

    def test_long_number(self):
        temp = Solution()
        self.value = 12345678987654321

        self.assertEqual(temp.isPalindrome(self.value), True)
    
    def test_negative_number(self):
        temp = Solution()
        self.value = -121
        self.assertEqual(temp.isPalindrome(self.value), False)
        
    def test_two_digits_false(self):
        temp = Solution()
        self.value = 12
        self.assertEqual(temp.isPalindrome(self.value), False)
    
    def test_input_one_digit(self):
        temp = Solution()
        self.value = 0
        self.assertEqual(temp.isPalindrome(self.value), True)


if __name__ == "__main__":
    unittest.main()
