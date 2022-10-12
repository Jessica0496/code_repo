from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        true_idx = []
        for i in range(n):
            if s[: i + 1] in word_set:
                true_idx.append(i)
            else:
                for j in true_idx:
                    if j < i and s[j + 1: i+1] in word_set:
                        true_idx.append(i)
                        break
        return True if true_idx and true_idx[-1] == n - 1 else False
s = Solution()
print('t', s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print('t', s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print('f',s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))