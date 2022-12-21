########################################
# Node class used to build trees 
########################################

class Node(object):
    data = None;
    left = None;
    right = None;

    def __init__(self, data):
        self.data = data;
        


########################################
# Different ordered tree print methods
########################################

def inorderPrint(root):
    if(root == None):
        return;
    inorderPrint(root.left);
    print(root.data, end = " ");
    inorderPrint(root.right);

def preorderPrint(root):
    if(root == None):
        return;
    print(root.data, end = " ");
    preorderPrint(root.left);
    preorderPrint(root.right);

def postorderPrint(root):
    if(root == None):
        return;
    postorderPrint(root.left);
    postorderPrint(root.right);
    print(root.data, end = " ");



########################################
# Building some test trees
########################################

bstTree = Node(100);
#Left Side
bstTree.left = Node(50);
bstTree.left.left = Node(10);           #              100
bstTree.left.left.left = Node(3);       #           /      \
bstTree.left.right = Node(75);          #        50          150
bstTree.left.right.left = Node(60);     #       /  \        /   \
bstTree.left.right.right = Node(80);    #     10   75     120   200   
#Right side                             #     /   /  \      \
bstTree.right = Node(150);              #    3   60  80     135
bstTree.right.left = Node(120);
bstTree.right.left.right = Node(135);
bstTree.right.right = Node(200);

#The errors here are the 50 and 21 in the bottom of the tree
nonBSTTree = Node(20);
#Left Side
nonBSTTree.left = Node(10);
nonBSTTree.left.left = Node(5);             #              20
nonBSTTree.left.left.left = Node(3);        #           /      \
nonBSTTree.left.right = Node(15);           #        10          40
nonBSTTree.left.right.left = Node(12);      #       /  \        /  \
nonBSTTree.left.right.right = Node(21);     #      5   15      30  50   
#Right side                                 #     /   /  \       \
nonBSTTree.right = Node(40);                #    3   12  21       50
nonBSTTree.right.left = Node(30);
nonBSTTree.right.left.right = Node(50);
nonBSTTree.right.right = Node(50);



########################################
# Binary search tree validator function
########################################

def inorderKeys(root):
    if(root == None):
        return [];

    keys = inorderKeys(root.left); 
    keys.append(root.data);
    keys += inorderKeys(root.right);
    
    return keys;

def isBST(root):
    inorder = inorderKeys(root);
    for i in range(len(inorder)-1):
        if(inorder[i] > inorder[i+1]):
            return False;

    return True;



########################################
# Testing order prints and 
# checking BST validity
########################################

inorderBSTKeys = inorderKeys(bstTree);
print("\nFirst is a valid BST: \t", isBST(bstTree));
print("Inorder print: ", end = "\t\t");
inorderPrint(bstTree);
print("\nPreorder print: ", end = "\t");
preorderPrint(bstTree);
print("\nPostorder print: ", end = "\t");
postorderPrint(bstTree);
print();

inorderNonBSTKeys = inorderKeys(nonBSTTree);
print("\nSecond is a valid BST: \t", isBST(nonBSTTree));
print("Inorder print: ", end = "\t\t");
inorderPrint(nonBSTTree);
print("\nPreorder print: ", end = "\t");
preorderPrint(nonBSTTree);
print("\nPostorder print: ", end = "\t");
postorderPrint(nonBSTTree);
print();
print();
