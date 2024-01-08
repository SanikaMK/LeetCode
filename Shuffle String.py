class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restored = ['']*len(s)
        print(restored)
        for i, char in enumerate(s):
            restored[indices[i]] = char
            print(restored[indices[i]])
            print(char)
        return ''.join(restored)