class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack =[]
        for token in tokens:
            if token == '+':
                stack.append(int(stack.pop())+int(stack.pop()))
            elif token == '*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif token == '-':
                poped = int(stack.pop())
                stack.append(int(stack.pop())-poped)
            elif token == '/':
                poped = int(stack.pop())
                stack.append(int(stack.pop())/poped)
            else:
                stack.append(token)
        return int(stack.pop())