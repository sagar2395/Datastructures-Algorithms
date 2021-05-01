namespace SolutionsInCSharp
{
    public class Solution12
    {
        public ListNode RotateRight(ListNode head, int k)
        {
            if(head == null || head.next == null || k ==0) return head;
            
            ListNode temp = head;
            int count = 1;
            while(temp.next != null){
                temp = temp.next;
                count++;
            }
        
            if(k >= count){
                k = k % count;
            }

            temp.next = head;

            ListNode lastNode = head;
            for(int i = 0 ; i < count - k - 1 ; i++){
                lastNode = lastNode.next;
            }
            head = lastNode.next;
            lastNode.next = null;

            return head;
        }
    }
}