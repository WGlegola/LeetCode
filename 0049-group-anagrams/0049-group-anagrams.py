class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {} 
        for word in strs:
            key = tuple(sorted(word)) # or a count tuple 
            groups.setdefault(key, []).append(word) 
        return list(groups.values())