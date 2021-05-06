using System;

namespace SolutionsInCSharp
{
    public class Solution21
    {
        public int DivideInteger(int dividend, int divisor)
        {
            if (divisor == 0)
                throw new DivideByZeroException();

            if (dividend == int.MinValue && divisor == -1)
                return int.MaxValue;

            return dividend / divisor;
        }
    }
}