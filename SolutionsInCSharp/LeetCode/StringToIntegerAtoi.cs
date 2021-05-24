using System;

namespace SolutionsInCSharp
{
    public class Solution23
    {
        public int MyAtoi(string s)
        {
            bool isNumberStarted = false;
            bool isPositive = true;
            string result = "";

            foreach (char a in s)
            {
                if (!isNumberStarted && !Char.IsDigit(a))
                {
                    if (Char.IsWhiteSpace(a) || a.Equals('+') || a.Equals('-'))
                    {
                        if (a == '-')
                        {
                            isPositive = false;
                            isNumberStarted = true;
                        }

                        if (a == '+')
                        {
                            isPositive = true;
                            isNumberStarted = true;
                        }
                        continue;
                    }
                    else
                    {
                        return 0;
                    }
                }

                if (Char.IsDigit(a))
                {
                    if (!isNumberStarted)
                    {
                        isNumberStarted = true;
                    }

                    result += a;
                }

                if (isNumberStarted && !Char.IsDigit(a))
                {
                    break;
                }
            }

            if (result == "") return 0;
        
            bool parse = int.TryParse(result , out int n);
        
            if(!parse){
                if(isPositive){
                    return 2147483647;
                }
                else{
                    return -2147483648;
                }
            }

            int final = Convert.ToInt32(result);

            return isPositive ? final : -final;
        }
    }
}