namespace SolutionsInCSharp
{
    public class Solution28
    {
        public ListNode RemoveElements(ListNode head, int val)
        {

            if (head == null) return null;

            while (head.val == val && head.next != null)
            {
                head = head.next;
            }

            if (head.val == val && head.next == null) return null;
            if (head.val != val && head.next == null) return head;

            ListNode temp = head.next;
            ListNode ln = head;

            while (temp.next != null)
            {
                if (temp.val == val)
                {
                    ln.next = temp.next;
                    temp = temp.next;
                }
                else
                {
                    ln = temp;
                    temp = temp.next;
                }
            }

            if (temp.val == val)
            {
                ln.next = null;
            }

            return head;

        }
    }
}