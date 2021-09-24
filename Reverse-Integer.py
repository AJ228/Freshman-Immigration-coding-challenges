class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = 0
        xCopy = int(str(x)[:]) #Used to form reversed integer
        power = len(str(abs(x))) - 1
        for i in range(len(str(x))): #Runs on all digits of x
            digits += (abs(xCopy) % 10) * (10 ** power) #Multiplies smallest digit by largest power
            power -= 1
            xCopy = abs(xCopy) // 10
        if x < 0:
            digits = -int(digits) #Adjusts sign of digits depending on sign of x
        if abs(digits) >= (2**31) - 1: #If reversed number is out of range, make digits 0
            digits = 0
        return digits
        