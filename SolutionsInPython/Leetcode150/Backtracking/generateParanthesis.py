# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]


from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            print("backtrack("+str(openN)+", "+str(str(closedN))+")")
            if openN == closedN == n:
                print("".join(stack))
                res.append("".join(stack))

            if openN < n:
                print("Inserting ( to path")
                stack.append("(")
                backtrack(openN + 1, closedN)
                k = stack.pop()
                print("Removing last bracket from stack " + k)

            if closedN < openN:
                print("Inserting ) to path")
                stack.append(")")
                backtrack(openN, closedN + 1)
                k = stack.pop()
                print("Removing last bracket from stack " + k)

        backtrack(0, 0)
        return res
    
a = Solution()
print(a.generateParenthesis(3))