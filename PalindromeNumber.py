class Solution:
    def isPalindrome(self, x):
        reverseNumber = 0
        tempX = int(x)  
        if(x < 0):
            return False

        for i in range(len(str(x))):
            reverseNumber = reverseNumber * 10
            reverseNumber = reverseNumber + tempX % 10
            tempX = tempX // 10

        if(reverseNumber == x):
            return True
        return False
