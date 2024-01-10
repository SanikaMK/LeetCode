class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        #print(words)
        restored = [""] * len(words)
        #print(restored)
        for word in words:
            #print(word)
            #print(word[:-1])
            position = int(word[-1]) - 1
            #print(position)
            actual_word = word[:-1]
            #print(actual_word)
            restored[position] = actual_word
            #print(restored[position])
        return " ".join(restored)
