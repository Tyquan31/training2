/*
	The binary and binary search trees

 	A node in a binary tree has two children at most: one left child and one right child. This definition allows us to write more efficient algorithms to insert, search, and delete nodes to/from a tree.

 	Instead of calling the node itself as a node or item, as we did in the previous chapters, we will call it a key. A key is how a tree node is known in tree terminology.

 	{3} - If the tree is not empty, we need to find a place to add a new node. For this reason, we will call the insertNode function by passing the root and the node as parameters

 	{4} - If the node's key is less than the current node key (in this case, it is the root (line {4} ))
	
	{5} - then we need to check the left child of the node. If there is no left node

	{6} - then we will insert the new node there

	{7} - If not, we need to descend a level in the tree by calling insertNode recursively

	{8} - If the node's key is greater than the current node key and there is no right child

	{9} - then we will insert the new node there

	{10} - If not, we will also need to call the insertNode function recursively, but the new node to be compared will be the right child

*/

class BinarySearchTree {
	constructor (key){
		this.key = key;
		this.left = null;
		this.right = null;
		this.root = null;
		// insert a new node to the tree
		this.insert = function(key) {
			var newNode = new BinarySearchTree(key);
			if (this.root === null) {
				this.root = newNode;
			} else {
				insertNode(this.root, newNode); // {3}
			}
		};
		// in-order traversal
		this.inOrderTraverse = function(callback) {
			inOrderTraverseNode(this.root, callback);
		}
	}
}

// function BinarySearchTree(){
// 	var Node = function(key) { // {1}
// 		this.key = key;
// 		this.left = null;
// 		this.right = null;
// 		this.insert = function(key) {
// 			var newNode = new Node(key);
// 			if (root === null) {
// 				root = newNode;
// 			} else {
// 				insertNode(root, newNode); // {3}
// 			}
// 		};
// 	};

// 	var root = null; // {2}
// }

function insertNode(node, newNode) {
	if (newNode.key < node.key) { // {4}
		if (node.left === null) { // {5}
			node.left = newNode // {6}
		} else {
			insertNode(node.left, newNode); // {7}
		}
	} else {
		if (node.right == null) { // {8}
			node.right = newNode; // {9}
		} else {
			insertNode(node.right, newNode); // {10}
		}
	}
}

function inOrderTraverseNode (node, callback) {
	if (node !== null) {
		inOrderTraverseNode(node.left, callback);
		callback(node.key);
		inOrderTraverseNode(node.right, callback);
	}
}

function printNode(value) {
	console.log(value);
}

/*
	Example
*/

var tree = new BinarySearchTree();
tree.insert(11);
tree.insert(7);
tree.insert(15);
tree.insert(5);
tree.insert(3);
tree.insert(9);
tree.insert(8);
tree.insert(10);
tree.insert(13);
tree.insert(12);
tree.insert(14);
tree.insert(20);
tree.insert(18);
tree.insert(25);

tree.inOrderTraverse(printNode);

//console.log(tree);