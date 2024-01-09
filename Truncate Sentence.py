class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        print(words)
        truncated = ' '.join(words[:k])
        print(truncated)
        return truncated