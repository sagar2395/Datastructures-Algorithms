using System.Collections.Generic;
using System.Linq;

namespace SolutionsInCSharp
{
    public class Solution37
    {
        public int MaximumPopulation(int[][] logs)
        {
            Dictionary<int, int> dict = new Dictionary<int, int>();

            foreach (var log in logs)
            {
                for (int i = log[0]; i < log[1]; i++)
                {
                    if (dict.ContainsKey(i))
                    {
                        dict[i] += 1;
                    }
                    else
                    {
                        dict[i] = 1;
                    }
                }
            }

            var list = dict.Keys.ToList();
            list.Sort();

            int maxPopulation = 0;
            int maxYear = 0;
            for (int j = 0; j < list.Count; j++)
            {
                if (dict[list[j]] > maxPopulation)
                {
                    maxPopulation = dict[list[j]];
                    maxYear = list[j];
                }
            }

            return maxYear;
        }
    }
}