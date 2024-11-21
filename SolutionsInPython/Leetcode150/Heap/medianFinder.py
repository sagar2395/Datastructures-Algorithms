# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

import heapq
class MedianFinder:
    def __init__(self):
        self.lo = []  
        self.hi = []  

    def addNum(self, num):
        heapq.heappush(self.lo, -num)             # lo is maxheap, so -1 * num
        heapq.heappush(self.hi, -self.lo[0])      # hi is minheap
        heapq.heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)
            
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]                  
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()