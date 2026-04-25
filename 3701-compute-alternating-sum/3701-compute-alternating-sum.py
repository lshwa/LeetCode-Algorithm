class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        answer = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                answer += nums[i]
            else:
                answer -= nums[i]

        return answer
        