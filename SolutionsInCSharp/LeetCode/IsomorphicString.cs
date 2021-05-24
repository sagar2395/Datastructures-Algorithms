using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution29
    {
        public bool IsIsomorphic(string s, string t)
        {
            var dict1 = new Dictionary<char, char>();
            var dict2 = new Dictionary<char, char>();

            if (s.Length != t.Length)
            {
                return false;
            }

            for (int i = 0; i < s.Length; i++)
            {
                if (!dict1.ContainsKey(s[i]) && !dict2.ContainsKey(t[i]))
                {
                    dict1.Add(s[i], t[i]);
                    dict2.Add(t[i], s[i]);
                }
                else if (dict1.ContainsKey(s[i]) && !dict2.ContainsKey(t[i]))
                {
                    return false;
                }
                else if (!dict1.ContainsKey(s[i]) && dict2.ContainsKey(t[i]))
                {
                    return false;
                }
                else if (dict1.ContainsKey(s[i]) && dict2.ContainsKey(t[i]))
                {
                    if (dict1[s[i]] == t[i])
                    {
                        continue;
                    }
                    return false;
                }
            }
            return true;
        }
    }
}