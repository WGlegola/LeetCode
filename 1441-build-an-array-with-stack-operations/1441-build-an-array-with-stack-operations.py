class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        iterator = iter(target)
        anweser = []
        currentTarget = next(iterator)

        for i in range(1,n+1):
            anweser.append('Push')
            if currentTarget != i:
                anweser.append('Pop')
            if currentTarget == i:
                try:
                    currentTarget = next(iterator)
                except BaseException:
                    break
        return anweser
                
            
