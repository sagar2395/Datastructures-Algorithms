using System.Collections.Generic;

namespace SolutionsInCSharp{
    public class Solution16{
        public IList<int> PreOrderTraversal(TreeNode root){
            IList<int> list = new List<int>();
            TreeNode temp = root;
            Stack<TreeNode> stck = new Stack<TreeNode>();

            if(root == null){
                return list;
            }

            stck.Push(temp);

            while(stck.Count > 0){
                TreeNode node= stck.Pop();
                list.Add(node.val);

                if(node.right != null){
                    stck.Push(node.right);
                }
                if(node.left != null){
                    stck.Push(node.left);
                }
            }

          return list;
        }
    }
}