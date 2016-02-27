#############################################################################################
#############################################################################################
##
## This code creates 50 binary search trees by randomnly selecting how many nodes to
## add to each tree and adding random integer values (as nodes) to each tree on the fly.
## The inorder traveral function traverses through each tree inorder, keeping note of the steps taken.
## The final result shows the number of nodes in each tree and the number of steps taken to traverse it.
## Looking at the result, it is clear the steps taken are 2(n-1) where n is the number of nodes in a tree
##
##
#############################################################################################
#############################################################################################


import pydot
import random

# Useful variables
graph = pydot.Dot(graph_type='graph')  # A crude yet effective representation of the bst in graphical form.
# Nodes are added to this graph on the fly.
# Final result of the graph can be written to output.png by calling graph.write_png('output.png')
edge = []  # Used to add nodes in the graph
count = 0  # Counter of the steps taken in inorder traversal function
inorderResult = []  # Stores the sequence of nodes visited or outputted by inorder function


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

        # Function to add nodes to the binary search tree on the fly

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            edge = pydot.Edge(" ", "%s" % key)
            graph.add_edge(edge)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                edge = pydot.Edge("%s" % currentNode.getKey(), "%s" % key)
                graph.add_edge(edge)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                edge = pydot.Edge("%s" % currentNode.getKey(), "%s" % key)
                graph.add_edge(edge)

                # get() and _get() functions are used to overload the [] operator.

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __setitem__(self, k, v):  # Overloads the [] operator
        self.put(k, v)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):  # overloads the 'in' operator.
        if self._get(key, self.root):
            return True
        else:
            return False

    def inorder(self, root):  # inOrder traversel function utilizing recursion
        global inorderResult
        global count
        if root.isLeaf():
            inorderResult.append(root.getKey())
            return

        if root.hasLeftChild():
            count += 2  # Each recursive call takes one step forward and one step back
            self.inorder(root.getLeftChild())  # Traversing left in the tree
            inorderResult.append(root.getKey())  # Visit current node

        if root.hasRightChild():
            count += 2
            self.inorder(root.getRightChild())  # Traversing right in the tree
            if not root.getKey() in inorderResult:
                inorderResult.append(root.getKey())

    def inorder_catch(self):
        self.inorder(self.root)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def getKey(self):
        return self.key




########
##  Binary tree creation and traversal starts here
#######

numberOfTrees = 50
numbferOfNodesPerTree = random.sample(xrange(50, 101), numberOfTrees)
print "Nodes\t\t\t\t\tSteps"
for x in numbferOfNodesPerTree:  # For each tree the number of nodes has been randomnly chosen
    myTree = []
    myTree = BinarySearchTree()  # Initializing tree
    count = 0  # Resetting steps for traversal function
    inorderResult = []  # Resetting result
    for y in random.sample(xrange(1, 101), x):  # Generating node values randomnly
        myTree.put(y, 'test')  # Adding nodes on the fly
        # New tree has been generated. Calling traversal function
    myTree.inorder_catch()
    # graph.write_png('output.png') #makes a grapgical representation of the bst.
                                    # Left and right positions of nodes not 100% accurate
                                    # but good for debugging

    print "%i---------------------------------------%i" % (len(myTree), count)
