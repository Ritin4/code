Python List

A python list is a dynamic array.

    lst = ["buns", "cheese", "bottle"]

- Elements are stored contiguously in memory (not linked nodes like a linked list).

- It can grow or shrink at runtime.

- Internally, it allocates extra capacity to support fast appends.

-       Indexing = O(1) ;
        Appending (amortized) = O(1) ;
        Inserting at the front = O(n) (shifts elements);
        Deleting in the middle = O(n);