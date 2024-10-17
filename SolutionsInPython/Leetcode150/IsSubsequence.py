class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
         
        while i < len(s):
            if j == len(t):
                return False
            else:
                if s[i] == t[j]:
                    i += 1
                j+= 1
                    
        return True
                 
                
        
                 