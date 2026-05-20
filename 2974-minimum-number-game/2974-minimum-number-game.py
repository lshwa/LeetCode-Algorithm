class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        answer = []

        nums.sort()

        for i in range(0, len(nums), 2):
            answer.append(nums[i + 1])
            answer.append(nums[i])
        
        return answer


        
        