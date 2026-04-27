class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        answer = []

        for item in nums:
            if item % 2 == 0:
                answer.append(0)
            else:
                answer.append(1)
        
        answer.sort()
        
        return answer