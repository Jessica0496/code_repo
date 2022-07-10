from typing import List
from collections import defaultdict
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        word2root = defaultdict(list)
        for idx, word in enumerate(words):
            if not word2root[word]:
                for root in dictionary:
                    if word.startswith(root):
                        word2root[word].append(root)
                word2root[word].sort(key=lambda x: len(x))
            if word2root[word]:
                words[idx] = word2root[word][0]
        return ' '.join(words)

