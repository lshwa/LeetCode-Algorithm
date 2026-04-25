class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_cnt = 0
        less_pivot = []
        more_pivot = []

        for i in range(len(nums)):
            if nums[i] == pivot:
                pivot_cnt += 1
                continue
            
            if nums[i] < pivot:
                less_pivot.append(nums[i])
            else:
                more_pivot.append(nums[i])
        
        for i in range(pivot_cnt):
            less_pivot.append(pivot)
        
        return less_pivot + more_pivot
        