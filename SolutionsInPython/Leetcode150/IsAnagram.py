class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if(len(t) != len(s)):
            return False
        
        dict = {}
        
        for a in t:
            if a not in dict:
                dict[a] = 1
            else: 
                dict[a] += 1
                
        for a in s:
            if a not in dict:
                return False
            elif dict[a] == 0:
                return False 
            else: 
                dict[a] -= 1
                
        return True