namespace SolutionsInCSharp
{
    public class Solution26
    {
        public ListNode RemoveNthFromEnd(ListNode head, int n)
        {
            if (head == null) return null;

            ListNode temp = head;
            int length = 1;
            while (temp != null)
            {
                temp = temp.next;
                length++;
            }
            if (length < n) return head;

            if (head.next == null && n == 1) return null;

            ListNode ln = head;
            int removalPosition = length - n - 1;

            if (removalPosition == 0) return head.next;

            for (int i = 0; i < removalPosition - 1; i++)
            {
                ln = ln.next;
            }

            ln.next = ln.next.next;

            return head;
        }

    }
}