using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution11
    {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        public int CountPrimes(int n)
        {
            int count = 0;
            for (int i = 2; i < n; i++)
            {

                bool isPrime = true;
                for (int j = 2; j < i; j++)
                {

                    int remainder = CheckRemainder(i, j);

                    if (remainder == 0)
                    {
                        isPrime = false;
                    }

                }

                if (isPrime) count++;
                dict.Clear();
            }

            return count;
        }

        public int CheckRemainder(int i, int j)
        {
            if (dict.ContainsKey(j))
            {
                return dict[j];
            }
            else
            {
                dict[j] = i % j;
                return dict[j];
            }

        }
    }

}