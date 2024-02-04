class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = " ".join(s.strip().split()[::-1])
        return s_split