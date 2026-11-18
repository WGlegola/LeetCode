class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        no = 0
        setli = set(words)
        for x, word in enumerate(words):
            if word in setli:
                setli.discard(word)
                word2 = word[::-1]
                if word2 in setli:
                    setli.discard(word)
                    no+=1
        return no
        