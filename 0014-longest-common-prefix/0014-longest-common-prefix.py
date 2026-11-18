class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        memory = strs[0]
        for i in strs[1:]:
            if i == "":
                return ""
            for j in range(len(i)):
                if j >= len(memory):
                    break
                elif i[j]!=memory[j]:
                    memory = memory[:j]
                elif j == len(i)-1:
                    memory=i
        return memory