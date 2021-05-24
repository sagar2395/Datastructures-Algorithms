namespace SolutionsInCSharp
{
    public class Solution30
    {
        public ListNode ReverseList(ListNode head)
        {
            ListNode current = head;
            ListNode previous = null;
            ListNode temp;

            while (current != null)
            {
                temp = current.next;
                current.next = previous;
                previous = current;
                current = temp;
            }

            return previous;
        }
    }
}