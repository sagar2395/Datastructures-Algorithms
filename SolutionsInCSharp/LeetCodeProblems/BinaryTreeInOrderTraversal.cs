using System.Collections.Generic;

namespace SolutionsInCSharp{
    public class Solution14{
        public IList<int> InOrderTraversal(TreeNode root){
              IList<int> list = new List<int>();
            TreeNode temp = root;
            Stack<TreeNode> stck = new Stack<TreeNode>();

            if(root == null){
                return list;
            }


            while(temp!= null || stck.Count > 0){
                while(temp!=null){
                    stck.Push(temp);
                    temp = temp.left;
                }

                temp = stck.Pop();
                list.Add(temp.val);

                temp = temp.right;
            }

            return list;
        }
    }
}