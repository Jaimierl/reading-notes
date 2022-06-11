# Stacks and Queues

Stacks remind me of yoyo strings. Imagine you have a yoyo and every inch of the string is painted a different colour. When the yoyo is in your hand, all of the string is wound from the bottom to the top. The coloured piece of string closest to your hand is the top of the stack. When you throw the yoyo down, if you have the skills I do, the yoyo will get stuck at the bottom. When the yoyo is fully unraveled, the painted piece of string closest to the yoyo ball is the bottom or has a value of 1. Rewinding the yoyo by hand is analogous to pushing an item onto the stack - it takes the same amount of time to wind another inch onto the yoyo. The only difference is that the string already is attached to the next color of string while for a stack you need to tell each item where its next item is by adding a pointer and the top has to be manually assigned to the last item added to the stack.

Queues are more like a line through the DMV. If you are first in line to enter, it will be your turn to leave first as well. Back in the day, they used to give people numbers to help everyone keep track of who's turn it was. Queues seem to follow a similar system where when the first item is removed from the queue, the pointer looks to the second item as the first in the "line" and when items are added, the item before knows the item that is next (like if I know that I am 5th in line, I would notice if someone came after me and was sixth).

According to [Codefellows](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html), common terminology needed for **stacks** are:
- Push - Nodes or items that are put into the stack are pushed
- Pop - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
- Top - This is the top of the stack.
- Peek - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
- IsEmpty - returns true when stack is empty otherwise returns false.

While **Queues** follow **First in First Out** and **Last In Last Out** with common terminology including:
- Enqueue - Nodes or items that are added to the queue.
- Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
- Front - This is the front/first Node of the queue.
- Rear - This is the rear/last Node of the queue.
- Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
- IsEmpty - returns true when queue is empty otherwise returns false.


[Reading Notes Home Page](README.md)