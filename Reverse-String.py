class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)-1,-1,-1): #Provides insertion index in reverse order
            movedChar = s.pop(0) #Pops character from the beginning of the string
            s.insert(i,movedChar) #Inserts popped character to provided index
        print(s) #To show string is being reversed

#Testing code works
solution1 = Solution()
solution1.reverseString(["h","e","l","l","o"])
solution1.reverseString(["1","2","3","4","5"])
solution1.reverseString(["H","a","n","n","a","h"])
solution1.reverseString(["h","i"," ","h","o","w"," ","a","r","e"," ","y","o","u"])