using System.Collections.Generic;

namespace SolutionsInCSharp
{
    public class MyStack
    {
        Queue<int> queue;
        /** Initialize your data structure here. */
        public MyStack()
        {
            queue = new Queue<int>();
        }

        /** Push element x onto stack. */
        public void Push(int x)
        {
            Queue<int> tempQueue = new Queue<int>();
            tempQueue.Enqueue(x);

            while (queue.Count != 0)
            {
                tempQueue.Enqueue(queue.Dequeue());
            }

            queue = tempQueue;

        }

        /** Removes the element on top of the stack and returns that element. */
        public int Pop()
        {
            return queue.Dequeue();
        }

        /** Get the top element. */
        public int Top()
        {
            return queue.Peek();
        }

        /** Returns whether the stack is empty. */
        public bool Empty()
        {
            return queue.Count == 0;
        }
    }
}