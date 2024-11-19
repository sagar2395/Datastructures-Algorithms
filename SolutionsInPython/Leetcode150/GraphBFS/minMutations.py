# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

# Example 2:
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2

from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1

        queue = deque([startGene])
        mutation = 0 

        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mutation

                for i in range(len(gene)):
                    for c in "ACGT":
                        mutated = gene[:i] + c + gene[i+1:]
                        if mutated in bankSet:
                            queue.append(mutated)
                            bankSet.remove(mutated)

            mutation += 1

        return -1