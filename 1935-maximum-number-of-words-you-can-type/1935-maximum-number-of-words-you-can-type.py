class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        answer = 0

        for word in words:
            can_type = True
            for ch in word:
                if ch in brokenLetters:
                    can_type = False
                    break

            if can_type:
                answer += 1
        
        return answer
