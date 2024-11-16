# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: path = "/home/"
# Output: "/home"

# Example 2:
# Input: path = "/home//foo/"
# Output: "/home/foo"

# Example 3:
# Input: path = "/home/user/Documents/../Pictures"
# Output: "/home/user/Pictures"

# Example 4:
# Input: path = "/../"
# Output: "/"

# Example 5:
# Input: path = "/.../a/../b/c/../d/./"
# Output: "/.../b/d"

class Solution(object):
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)
