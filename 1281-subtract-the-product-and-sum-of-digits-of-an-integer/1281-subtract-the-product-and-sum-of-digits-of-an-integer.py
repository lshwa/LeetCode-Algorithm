class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        answer = 0
        suma, prod = 0, 1

        for digit in str(n):
            suma += int(digit)
            prod *= int(digit)
        
        answer = prod - suma

        return answer
        
        
        