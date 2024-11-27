# 38. Count and Say
# https://leetcode.com/problems/count-and-say/description/

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

# Example 2:
# Input: n = 1
# Output: "1"
# Explanation:
# This is the base case.

class Solution:
    def countAndSay(self, n: int) -> str:
        
        result = "1"

        for i in range(2, n + 1):
            s = 0
            e = 0
            temp = ""
            while e < len(result):

                while e < len(result) and result[e] == result[s] :
                    e += 1
                count = e - s
                temp += str(count) + result[e-1]
                s = e
            result = temp 

        return result

            


            