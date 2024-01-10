class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set("abcdefghijklmnopqrstuvwxyz")
        sent_char = set(sentence)
        return  alphabets.issubset(sent_char)