namespace SolutionsInCSharp
{
    public class Solution36
    {
        public bool IsPathCrossing(string path)
        {
            int length = path.Length + 1;
            int[][] arr = new int[length][];

            arr[0] = new int[2] { 0, 0 };
            int i = 1;
            foreach (var direction in path)
            {
                switch (direction)
                {
                    case 'N':
                        arr[i] = new int[2] { arr[i - 1][0], arr[i - 1][1] + 1 };
                        break;
                    case 'S':
                        arr[i] = new int[2] { arr[i - 1][0], arr[i - 1][1] - 1 };
                        break;
                    case 'W':
                        arr[i] = new int[2] { arr[i - 1][0] - 1, arr[i - 1][1] };
                        break;
                    case 'E':
                        arr[i] = new int[2] { arr[i - 1][0] + 1, arr[i - 1][1] };
                        break;
                }
                for (int j = 0; j < i; j++)
                {

                    if (arr[j][0] == arr[i][0] && arr[j][1] == arr[i][1])
                    {
                        return true;
                    }
                }

                i++;
            }

            return false;
        }
    }
}