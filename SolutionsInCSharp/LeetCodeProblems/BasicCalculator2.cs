using System.Collections.Generic;
using System;

namespace SolutionsInCSharp
{
    public class Solution13
    {

        //Not passing all test cases 
        public int Calculate(string s)
        {
            Stack<int> stck = new Stack<int>();

            int result = 0;
            bool next = false;
            bool positive = false;
            int i = 0;
            foreach (char a in s)
            {
                if (next)
                {
                    if (positive)
                    {
                        stck.Push(a);
                    }
                    else
                    {
                        stck.Push(-a);
                    }

                    next = false;
                    positive = true;
                }
                else
                {
                    if (char.IsDigit(a) && stck.Count != 0)
                    {
                        int num = stck.Pop() * 10 + Convert.ToInt32(a);
                        stck.Push(num);
                    }
                    else if (stck.Count == 0)
                    {
                        if (char.IsDigit(a))
                        {
                            stck.Push(Convert.ToInt32(a));
                        }
                        else
                        {
                            next = true;
                            positive = false;
                        }
                    }
                    else
                    {
                        if (a == '+')
                        {
                            next = true;
                            positive = true;
                        }
                        else if (a == '-')
                        {
                            next = true;
                            positive = false;
                        }
                        else if (a == '/')
                        {
                            int num1 = Convert.ToInt32(s[i + 1]);
                            int num2 = stck.Pop();
                            result += num1 / num2;
                        }
                        else if (a == '*')
                        {
                            int num1 = Convert.ToInt32(s[i + 1]);
                            int num2 = stck.Pop();
                            result += num1 * num2;
                        }
                    }
                    i++;
                }

                while (stck.Count != 0)
                {
                    result += stck.Pop();
                }
            }

            return result;
        }
    }
}