class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups={}
        for stri in strings:
            if len(stri) ==1:
                key = (0)
            else:
                key = tuple((ord(stri[i+1]) - ord(stri[i])) % 26 for i in range(len(stri) - 1))
            groups.setdefault(key,[]).append(stri)
        return list(groups.values())