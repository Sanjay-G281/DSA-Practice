class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        S = s.split()
        l = S[-1]
        return len(l)
