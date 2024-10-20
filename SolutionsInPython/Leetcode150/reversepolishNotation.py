class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isnumeric():
                token = int(token)
                stack.append(token)
            elif token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                sum = num1 + num2
                stack.append(sum)
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                mul = num1 * num2
                stack.append(mul)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                div = int(num2 / num1)
                stack.append(div)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                sub = num2 - num1
                stack.append(sub) 
                
        return stack.pop()
    
a = Solution()
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

print(int(6//-132))