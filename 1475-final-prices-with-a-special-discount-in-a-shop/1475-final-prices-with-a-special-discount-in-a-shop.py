class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        anwsers = []
        for index, item in enumerate(prices):
            discount = 0 
            if index==len(prices)-1:
                anwsers.append(item)
                break
            for promo in prices[index+1:]:
                if promo<=item:
                    discount = promo
                    break
            anwsers.append(item-discount)
        return anwsers
