class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for letter in magazine:
            if letter not in dict:
                dict[letter] = True
        print(dict)
                
        for letter in ransomNote:
            if letter not in dict:
                return False
            
        return True
        
        
ransom = Solution()

ransom.canConstruct("aa", "aab")