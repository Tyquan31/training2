# Tree Data Structure

> Trees are one of the most advanced and complex data structures out there. It opens doors to graph theory, which is used to represent a relationship between objects. The objects can be of any type, and as long as they have an established relationship, it can be represented in the form of a tree.

> very useful for storing information that needs to be found easily

> A tree is an abstract model of a hierarchical structure. The most common example of a tree in real life would be a family tree or a company organizational chart

## Tree terminology

> A tree consists of nodes with a parent-child relationship. Each node has a parent (except for
the first node at the top) and zero or more children

> The top node of a tree is called the root (11). It is the node that does not have a parent. Each
element of the tree is called a node. There are internal nodes and external nodes. An
internal node is a node with at least one child (7,5,9,15,13, and 20 are internal nodes). A
node that does not have children is called an external node or leaf (3,6,8,10,12,14,18, and 25
are leaves).

> A node can have ancestors and descendants. The ancestors of a node (except the root) are
parent, grandparent, great-grandparent, and so on. The descendants of a node are children
(child), grandchildren (grandchild), great-grandchildren (great-grandchild), and so on.

> The depth of a node consists of the number of ancestors. For example, node 3 has a depth of
3 because it has three ancestors (5,7, and 11).

> The height of a tree consists of the maximum depth of any node. A tree can also be broken
down into levels. The root is on level 0, its children are on level 1, and so on. The tree from
the preceding diagram has a height of 3

## The binary and binary search trees

> A node in a binary tree has two children at most: one left child and one right child. This
definition allows us to write more efficient algorithms to insert, search, and delete nodes
to/from a tree. Binary trees are largely used in computer science.

### Creating the BinarySearchTree class

> binary.js

> Instead of calling the node itself as a node or item, as we did in the previous chapters, we will call it a key. A key is how a tree node is known in tree terminology.

### Inserting a key into a tree

> To insert a new node (or item) into a tree, there are three steps we need to follow.

	1. The first step is to create the instance of the Node class that will represent the new node (line {1} ). Because of its constructor properties, we only need to pass the value we want to add to the tree, and its left and right pointers will have a null value automatically.

	2. Second, we need to verify that the insertion is a special case. A special case would be if the node we are trying to add is the first one in the tree (line {2} ). If it is, all we have to do is point the root to this new node.

	3. The third step is to add a node to a different position than the root. In this case, we will need a helper (line {3} ) private function to help us to do this

> binary.js

> The insertNode function will help us find out where the correct place to insert a new node
is

## In-order Traversal

> An in-order traversal visits all the nodes of a BST in an ascending order, meaning it will
visit the nodes from the smallest to the largest. An application of in-order traversal would
be to sort a tree.

> binary.js