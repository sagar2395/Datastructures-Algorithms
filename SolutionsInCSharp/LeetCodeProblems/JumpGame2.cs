using System;

namespace SolutionsInCSharp{
    public class Solution38{
        public int Jump(int[] nums){
            if(nums.Length == 1) return 0;

            int currentCoverage = nums[0];
            int lastJumpIndex = 0;
            int jumpCount = 0;

            for(int i = 0 ; i < nums.Length ; i++){
                currentCoverage = Math.Max(currentCoverage , i + nums[i]);

                if(i == lastJumpIndex){
                    lastJumpIndex = currentCoverage;
                    jumpCount++;
                    if(currentCoverage >=nums.Length - 1){
                        return jumpCount;
                    }
                }
            }

            return jumpCount;

        }
    }
}