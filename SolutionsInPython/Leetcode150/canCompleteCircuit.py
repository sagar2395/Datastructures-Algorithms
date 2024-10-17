class Solution(object):
    def canCompleteCircuit(self, gas):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        for i in range(len(gas)):
            print("Cycle: ", str(i))
            for j in range(i, len(gas)):
                print(j)
            for j in range(i):
                print(j)
                

c = Solution()
gas = [1, 2, 3, 4, 5]
c.canCompleteCircuit(gas)