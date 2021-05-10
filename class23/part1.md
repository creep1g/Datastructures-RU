## Part 1

1. Look at the image of the heap
    1. What happens when the value 23 is added?
        * Firstly 23 is added to the next node from last inserted node, in this case that node is 9, so 23 will be placed right of 9, next 23 is compared to its parent node 7 since 7 is less than 23, 23 stays where it is
    2. What happens when the value 1 is added?
        * Firstly 1 is added to the next available spot on the heap, in this case it is right child of 7, next 1 is compared to its parent node which is 7, since 7 is greater than 1 7 and 1 swap places, again we compare to the parent node which is now root(2) since 1 is less than root 1 swaps with two. now 1 is root and right child of root is 2
    3. What happens when the value 14 is added after the value 1 has been added?
        * 14 is placed on the next available node, this time it is left child of 16, since both sub trees are full a new node is added as the leftmost of a new level. next we compare 14 to 16 since 16 is greater than 14 they swap places, now 14 is the parent of 16, next we compare 14 and 13, since 13 is less than 14, 14 stays where it is.
    4. What happens when a value is removed?
        * When a value is removed only the root is removed and the rightmost of the bottommost level of the tree is put in its place, after that we start comparing, the child with the highest priority/ lowest value will swap with our new root, if root is already the smallest the algorithm stops, otherwise we move down the heap until our value is a node with no children or only has children that contain larger values than it self.

2. Look at the image of a hash table
    1. What happens when the value 9 is added?
    2. What happens when the value 18 is added?
    3. What happens when the value 12 is removed?
    4. What happens when the value 7 is removed?

3. Look at the image of a binary search tree
    1. What happens when the value 21 is added?
    2. What happens when the value 10 is added?
    3. What happens when the value 17 is added?
    4. What happens when the value 19 is removed?
    5. What happens when the value 13 is removed?


