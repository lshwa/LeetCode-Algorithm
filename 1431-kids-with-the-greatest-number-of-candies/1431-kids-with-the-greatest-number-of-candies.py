class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        answer = []

        for candy in candies:
            if candy + extraCandies >= max_candy:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
