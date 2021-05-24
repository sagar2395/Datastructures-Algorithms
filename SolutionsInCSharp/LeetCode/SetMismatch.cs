namespace SolutionsInCSharp
{
    public class Solution33
    {
        public int[] FindErrorNums(int[] nums)
        {
            if (nums == null || nums.Length == 0)
                return new int[] { };

            int[] res = new int[2],
                  arr = new int[nums.Length + 1];

            foreach (var item in nums)
                arr[item] += 1;

            for (int i = 1; i < arr.Length; i++)
                if (arr[i] == 2)
                    res[0] = i;
                else if (arr[i] == 0)
                    res[1] = i;

            return res;
        }
    }
}