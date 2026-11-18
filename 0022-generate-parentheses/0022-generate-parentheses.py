class Solution:
    def recur(self, anws, n):
        if n==0:
            return '()'
        an = []
        for i in range(n):
            an.append((lambda x:'('*n + x +')'*n)(self.recur(anws,n-1)))
        return an



    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current, open, close):
            # Kiedy dodać do wyniku?
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Kiedy możesz dodać '('?
            if open < n:
                backtrack(current + '(', open + 1, close)
            
            # Kiedy możesz dodać ')'?
            if close<open:  # ← uzupełnij warunek
                backtrack(current + ')', open, close + 1)
        
        backtrack("", 0, 0)
        return result