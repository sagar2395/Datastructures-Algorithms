using System;

namespace SolutionsInCSharp
{
    public class Solution35
    {
        public int FindNumbers1(int[] nums)
        {
            var count = 0;
            int length;
            foreach (var num in nums)
            {
                length = num.ToString().Length;
                if (length % 2 == 0) count++;
            }
            return count;
        }

        public int FindNumbers2(int[] nums)
        {
            var count = 0;
            int length;

            foreach (var num in nums)
            {
                length = 0;
                var temp = num;
                do
                {
                    temp = temp / 10;
                    length++;
                }
                while (Math.Abs(temp) >= 1);
                if (length % 2 == 0) count++;
            }
            return count;
        }
    }
}