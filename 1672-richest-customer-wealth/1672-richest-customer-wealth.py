class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = []

        for i in range(len(accounts)):
            answer.append(sum(accounts[i]))
        
        return max(answer)