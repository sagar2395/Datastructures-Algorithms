class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        
        if len(words) != len(pattern):
            return False
        
        dict = {}
        for i in range(len(words)):
            if words[i] not in dict:
                dict[words[i]] = pattern[i]
            elif dict[words[i]] != pattern[i]:
                return False
        
        dict2 = {}
        for i in range(len(words)):
            if pattern[i] not in dict2:
                dict2[pattern[i]] = words[i]
            elif dict2[pattern[i]] != words[i]:
                return False
            
        return True
        
        
        
a = Solution()

print(a.wordPattern("abba", "dog cat cat dog"))