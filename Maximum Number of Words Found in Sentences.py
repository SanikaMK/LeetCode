class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentences in sentences:
            word_count = len(sentences.split())
            if word_count > max_words:
                max_words = word_count
        return max_words
        