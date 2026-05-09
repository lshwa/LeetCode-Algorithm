class Solution:
    def interpret(self, command: str) -> str:
        answer = ''

        for idx in range(len(command)):
            if command[idx] == "G":
                answer += 'G'
            
            elif command[idx] == "(" and command[idx+1] == ")":
                answer += 'o'
                idx += 1
            
            elif command[idx] == "(" and command[idx + 1] == "a":
                answer += 'al'
                idx += 3
            
        return answer 

        