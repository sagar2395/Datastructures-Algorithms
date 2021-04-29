using System;
using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class Solution08
    {
        public bool isValidSudoku(char[][] board)
        {

            for (int i = 0; i < board.Length; i++)
            {
                HashSet<int> set = new HashSet<int>();
                for (int j = 0; j < board.Length; j++)
                {

                    if(board[i][j] == '.')continue;
                    int val = board[i][j] - '0';
                    if (!set.Contains(val))
                    {
                        set.Add(val);
                    }
                    else
                    {
                        return false;
                    }
                }
            }

            for (int i = 0; i < board.Length; i++)
            {
                HashSet<int> set = new HashSet<int>();
                for (int j = 0; j < board.Length; j++)
                {
                    if(board[j][i] == '.')continue;
                    int val = board[j][i] - '0';
                    if (!set.Contains(val))
                    {
                        set.Add(val);
                    }
                    else
                    {
                        return false;
                    }
                }
            }

            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    var row = i * 3;
                    var column = j * 3;
                    HashSet<int> set = new HashSet<int>();

                    for (int m = row; m < row + 3; m++)
                    {
                        for (int n = column; n < column + 3; n++)
                        {
                            if(board[m][n] == '.')continue;
                            var value = board[m][n] - '0';
                            if (!set.Contains(value))
                            {
                                set.Add(value);
                            }
                            else
                            {
                                return false;
                            }
                        }
                    }

                }
            }

            return true;
        }
    }
}