class Solution(object):
    def reverseString(self, s):
        #Challenge parameters
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)-1,-1,-1): #Provides insertion index in reverse order
            movedChar = s.pop(0) #Pops character from the beginning of the string
            s.insert(i,movedChar) #Inserts popped character to provided index
        print(s) #To show string is being reversed

###Testing code works correctly
solution1 = Solution()
print("Testing reverseString()...",end="")
s = ["h","e","l","l","o"]
solution1.reverseString(s)
assert(s == ["o","l","l","e","h"])
s = ["1","2","3","4","5"]
solution1.reverseString(s)
assert(s == ["5","4","3","2","1"])
s = ["H","a","n","n","a","h"]
solution1.reverseString(s)
assert(s == ["h","a","n","n","a","H"])
s = ["h","i"," ","h","o","w"," ","a","r","e"," ","y","o","u"]
solution1.reverseString(s)
assert(s == ["u","o","y"," ","e","r","a"," ","w","o","h"," ","i","h"])
print("Passed!")
