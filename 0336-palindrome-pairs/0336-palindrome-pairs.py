class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        no = set()
        dictli = {w:i for i,w in enumerate(words)} 
        for word in words:
            for n in range(len(word)+1):
                left=word[n:]
                right=word[:n]
                if left == left[::-1] and right[::-1] in dictli and dictli[word] != dictli[right[::-1]]:
                    
                    no.add((dictli[word],dictli[right[::-1]]))
                if right == right[::-1] and left[::-1] in dictli and dictli[word] != dictli[left[::-1]]:
                    no.add((dictli[left[::-1]],dictli[word]))
            if len(word) == 0:
                for spam in words:
                    if spam == word or spam != spam[::-1]:
                        continue
                    no.add((dictli[spam],dictli[word]))
                    no.add((dictli[word],dictli[spam]))
        return list(no)