class Solution:
    def minElement(self, nums: List[int]) -> int:
        number = []
        

        for num in nums:
            elem = 0

            for ch in str(num):
                elem += int(ch)
            number.append(elem)
        
        number.sort()

        return number[0]
                

        