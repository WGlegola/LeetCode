class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        romanValues = {"I":1,"V":5, "X": 10, "L":50, "C": 100, "D": 500, "M" :1000}
        # print(romanValues["I"])
        lastChar="A"
        for i in range(len(s)):
            num+=romanValues[s[i]]
            if s[i] == "V" and lastChar == "I":
                lastChar = "A"
                num-=2
            elif s[i] == "X" and lastChar == "I":
                lastChar = "A"
                num-=2
            elif s[i] == "L" and lastChar == "X":
                lastChar = "A"
                num-=20
            elif s[i] == "C" and lastChar == "X":
                lastChar = "A"
                num-=20
            elif s[i] == "D" and lastChar == "C":
                lastChar = "A"
                num-=200
            elif s[i] == "M" and lastChar == "C":
                lastChar = "A"
                num-=200
            lastChar=s[i]
        return num

