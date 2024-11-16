# 1791. Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/description/?envType=problem-list-v2&envId=graph&difficulty=EASY&status=TO_DO

# Example 1:
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

# Example 2:
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

from typing import List

class Solution:
    #  This approach iterates over entire array and updates the count in hashmap. It retur
    def findCenter(self, edges: List[List[int]]) -> int:
        
        hm = {}

        for edge in edges:
            hm[edge[0]] = 1 + hm.get(edge[0], 0)
            hm[edge[1]] = 1 + hm.get(edge[1], 0)

        for key in hm.keys():
            print(hm[key])
            if hm[key] == len(edges):
                return key

        return -1 
    
    # This approach just compares initial 2 items and returns the common one.
    def findCenter(self, edges: List[List[int]]) -> int:
        
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1] 