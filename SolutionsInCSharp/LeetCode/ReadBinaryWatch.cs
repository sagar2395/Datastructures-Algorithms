using System;
using System.Collections.Generic;
using System.Linq;

namespace SolutionsInCSharp
{
    public class Solution39
    {
        int CountOfOnes(int num)
        {
            var ones = 0;
            while (num > 0)
            {
                if (num % 2 == 1)
                {
                    ones++;
                }
                num /= 2;
            }
            return ones;
        }

        public IList<string> ReadBinaryWatch(int num)
        {
            if (num > 10)
            {
                return new List<string>();
            }
            if (num == 0)
            {
                return new List<string> { "0:00" };
            }

            var dict0 = Enumerable.Range(0, 60).ToDictionary(i => i, i => CountOfOnes(i));
            var dict1 = Enumerable.Range(0, 12).ToLookup(i => dict0[i], i => i);
            var dict2 = Enumerable.Range(0, 60).ToLookup(i => dict0[i], i => i);

            var list = new List<string>();
            for (var i = Math.Max(0, num - 6); i <= 4 && i <= num; i++)
            {
                foreach (var h in dict1[i])
                {
                    foreach (var m in dict2[num - i])
                    {
                        list.Add($"{h}:{m:00}");
                    }
                }
            }
            return list;
        }
    }
}