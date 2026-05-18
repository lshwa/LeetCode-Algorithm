class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        answer = []
        
        for digit in digits:
            nums += str(digit)
        
        nums = int(nums) + 1

        for ch in str(nums):
            answer.append(int(ch))
        
        return answer