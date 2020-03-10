class Solution:
    def isPalindrome(self, input):
        reverseNumber = 0
        tempinput = int(input)
        
        if(type(input) != type(int())):
            return None
        
        if(input < 0):
            return False

        for i in range(len(str(input))):
            reverseNumber = reverseNumber * 10
            reverseNumber = reverseNumber + tempinput % 10
            tempinput = tempinput // 10

        if(reverseNumber == input):
            return True
        return False
