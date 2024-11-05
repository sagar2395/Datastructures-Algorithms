# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation:
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Explanation:
# There is no concatenated substring.

# Example 3:
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# Explanation:
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

from typing import Counter, List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen = len(words[0])
        wslen = len(words) * len(words[0])

        res = []

        for pos in range(wlen):
            i = pos
            d = Counter(words)

            for j in range(i, len(s) + 1 - wlen, wlen):
                word = s[j: j + wlen]
                d[word] -= 1

                while d[word] < 0:
                    d[s[i: i + wlen]] += 1
                    i += wlen
                if i + wslen == j + wlen:
                    res.append(i)

        return res