class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for x in nums:
            max_or |= x

        count = 0

        def dfs(index, current_or):
            nonlocal count

            if index == len(nums):
                if current_or == max_or:
                    count += 1
                return

            # nums[index]를 선택하지 않음
            dfs(index + 1, current_or)

            # nums[index]를 선택함
            dfs(index + 1, current_or | nums[index])

        dfs(0, 0)
        return count