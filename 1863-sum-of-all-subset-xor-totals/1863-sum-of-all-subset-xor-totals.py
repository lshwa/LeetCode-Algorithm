class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.answer = 0

        def dfs(i, cur_xor):
            if i == len(nums):
                self.answer += cur_xor
                return
            
            dfs(i + 1, cur_xor)
            dfs(i + 1, cur_xor ^ nums[i])
        
        dfs(0,0)
        return self.answer