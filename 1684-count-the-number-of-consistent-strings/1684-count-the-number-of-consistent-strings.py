class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        for word in words:
            flag = True

            for i in range(len(word)):
                if word[i] not in allowed:
                    flag = False
                
            if flag == True:
                answer += 1
        
        return answer 
            
