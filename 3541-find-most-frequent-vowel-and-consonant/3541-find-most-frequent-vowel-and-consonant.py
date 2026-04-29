from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = Counter(s)

        max_vowel = 0
        max_consonant = 0

        for ch, cnt in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, cnt)
            else:
                max_consonant = max(max_consonant, cnt)

        return max_vowel + max_consonant
