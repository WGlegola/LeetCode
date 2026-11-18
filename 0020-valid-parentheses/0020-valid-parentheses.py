class Solution:
    def isValid(self, s: str) -> bool:
        memory = []
        for i in range(len(s)):
            if s[i] == ")":
                if len(memory) == 0:
                    return False
                if memory.pop() != "(":
                    return False
            elif s[i] == "]":
                if len(memory) == 0:
                    return False
                if memory.pop() != "[":
                    return False
            elif s[i] == "}":
                if len(memory) == 0:
                    return False
                if memory.pop() != "{":
                    return False
            else:
                memory.append(s[i])
        if len(memory) > 0:
            return False
        else: 
            return True