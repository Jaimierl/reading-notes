# Trees

Recursively searching through trees is an interesting application of using the call stack. To traverse through a tree, the first element is added to the call stack. 

In the case of the depth first [example in the reading](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html) where a pre-order traversal was done on a binary tree, the root was first added to the call stack. Then, as we moved through the nodes of the tree (in this case going from left to right) the next left child/parent node would be added to the call stack. 

The function only executes when it reaches a pure child node or a node without any additional children  for that branch. Then, since the previous parent/child and root nodes are still in the call stack, the function will go back towards the root one level and then back down through to the furthest leaves before executing again. 

Contrarily, a breadth first search is returns all of the elements in a tree on a level instead of all of the elements in a branch. To traverse breadth-first a queue is used instead of a stack. THe root is put into the front of the queue (where it is first to be removed from the queue). Its children are added to the rear of the queue. As the function executes, you will move to the next child in the tree, add its children to the end of the queue, and proceed. 

As the name suggests, binary trees can only have two children per node so nodes can be assigned by left and right. K-ary trees can have nodes with unlimited children. TO add a new node to a binary tree, you can just fill something in to an empty space from the top of the tree down (a breadth first traversal can help you find the ideal location). 

Binary trees are O(N) time with the n being the number of nodes and O(n) space with the n for space being the width of the tree.

A binary search tree is an organized binary tree in which the values larger than the node are added to the right and the values smaller than the node are added to the left of the tree. These have Big O(N) Of the height of the tree and the space complexity of BigO(1) since nothing would need to add to the space of the search. 

[Reading Notes Home Page](README.md)