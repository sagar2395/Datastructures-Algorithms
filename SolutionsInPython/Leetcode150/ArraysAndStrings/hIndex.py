# 274. H-Index
# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

from typing import List
class Solution(object):
    # unoptimized
    # Time complexity - O(n2)
    # Space complexity - O(n)
    def hIndex(self, citations: List[int]) -> int:
        papers = [0] * len(citations)

        for i in range(len(citations)):
            for j in range(min(citations[i], len(citations))):
                papers[j] += 1
        
        hIndex = 0
        for i in range(len(papers) - 1, -1 ,-1):
            if papers[i] >= i + 1:
                hIndex = i + 1
                break

        return hIndex
    
    # Optimized function
    # Time complexity - O(n)
    # Space complexity - O(n)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)

        paper_counts = [0] * (n+1)

        for c in citations:
            paper_counts[min(n, c)] += 1

        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]

        return h