using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution20
    {
        public bool IsValid(string s)
        {
            Stack<char> stck = new Stack<char>();

            foreach (char a in s)
            {
                if (a == '(' || a == '{' || a == '[')
                {
                    stck.Push(a);
                }
                else if (a == ')' || a == '}' || a == ']')
                {
                    char temp;
                    if (stck.Count != 0)
                    {
                        temp = stck.Pop();
                    }
                    else
                    {
                        return false;
                    }

                    if (
                         (temp == '(' && (a == '}' || a == ']'))
                      || (temp == '{' && (a == ')' || a == ']'))
                      || (temp == '[' && (a == '}' || a == ')')))
                    {
                        return false;
                    }
                }
            }

            if (stck.Count != 0) return false;
            return true;
        }
    }
}