class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        
        for item in nums:
            if nums.count(item) > 1 and item not in answer:
                answer.append(item)
            
        return answer
        