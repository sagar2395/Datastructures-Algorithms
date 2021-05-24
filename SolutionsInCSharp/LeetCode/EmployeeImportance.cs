using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution32
    {
        int result = 0;
        Dictionary<int, Employee> dict = new Dictionary<int, Employee>();
        public int GetImportance(IList<Employee> employees, int id)
        {
            for (int i = 0; i < employees.Count; i++)
            {
                dict[employees[i].id] = employees[i];
            }
            CalculateImportance(id);
            return result;
        }

        public void CalculateImportance(int id)
        {
            result += dict[id].importance;
            foreach (var item in dict[id].subordinates)
            {
                CalculateImportance(item);
            }
        }
    }
}