from graphics import *;

########################################
# Class structures for node/rbtree
########################################
class Node(object):
    key = None;
    right = None;
    left = None;
    color = False; 
    p = None;

    def __init__(self, key):
        self.key = key;

    def __int__(self):
        return key;

class RBTree(object):
    nil = None;
    root = None;

    def __init__(self):
        self.nil = Node(None);
        self.nil.color = True;
        self.root = self.nil;
        self.root.color = True;



########################################
# Functions necessary to insert 
# into RB tree
########################################

def rbInsert(tree, node):
    y = tree.nil;
    x = tree.root;
    #iterate to correct location
    while(x != tree.nil):
        y = x;
        if(node.key < x.key):
            x = x.left;
        else:
            x = x.right;
    #setup newNode in tree
    node.p = y;
    if(y == tree.nil):
        tree.root = node;
    elif(node.key < y.key):
        y.left = node;
    else:
        y.right = node;
    node.left = tree.nil;
    node.right = tree.nil;
    node.color = False;

    rbInsertFixup(tree, node);

def rbInsertFixup(tree, node):
    while(not node.p.color):
        if(node.p == node.p.p.left):
            y = node.p.p.right;
            #check case 1
            if(not y.color):
                node.p.color = True;
                y.color = True;
                node.p.p.color = False;
                node = node.p.p;
            else:
                #check case 2
                if(node == node.p.right):
                    node = node.p
                    leftRotation(tree, node);
                #run case 3
                node.p.color = True;
                node.p.p.color = False;
                rightRotation(tree, node.p.p);
        else:
            y = node.p.p.left;
            #check case 1
            if(not y.color):
                node.p.color = True;
                y.color = True;
                node.p.p.color = False;
                node = node.p.p;
            else:
                #check case 2
                if(node == node.p.left):
                    node = node.p
                    rightRotation(tree, node);
                #run case 3
                node.p.color = True;
                node.p.p.color = False;
                leftRotation(tree, node.p.p);
    tree.root.color = True;

########################################
# Rotation methods
########################################

def leftRotation(tree, node):
    y = node.right;
    node.right = y.left;
    if(y.left != tree.nil):
        y.left.p = node;
    y.p = node.p;
    if(node.p == tree.nil):
        tree.root = y;
    elif(node == node.p.left):
        node.p.left = y;
    else:
        node.p.right = y;
    y.left = node;
    node.p = y;

def rightRotation(tree, node):
    y = node.left;
    node.left = y.right;
    if(y.right != tree.nil):
        y.right.p = node;
    y.p = node.p;
    if(node.p == tree.nil):
        tree.root = y;
    elif(node == node.p.right):
        node.p.right = y;
    else:
        node.p.left = y;
    y.right = node;
    node.p = y;



########################################
# Other RBTree functions
########################################

def treeSuccessor(tree, node):
    if(node.right != tree.nil):
        #loop to get right subtree minimum
        temp = node.right;
        while(temp.left != tree.nil):
            temp = temp.left;
        return temp;
    
    y = node.p;
    while(y != tree.nil and node == y.right):
        x = y;
        y = y.p;
    return y;

def rbDelete(tree, node):
    if(node.left == tree.nil or node.right == tree.nil):
        y = node;
    else:
        y = treeSuccessor(tree, node);

    if(y.left != tree.nil):
        x = y.left;
    else:
        x = y.right;

    x.p = y.p;
    if(y.p == tree.nil):
        tree.root = x;
    elif(y == y.p.left):
        y.p.left = x;
    else:
        y.p.right = x;

    if(y != node):
        node.key = y.key;
    if(y.color):
        rbDeleteFixup(tree, x);
    return y;

def rbDeleteFixup(tree, node):
    while(node != tree.root and node.color):
        if(node == node.p.left):
            w = node.p.right;
            if(not w.color):
                w.color = True;
                node.p.color = False;
                leftRotation(tree, node.p);
                w = node.p.right;
            if(w.left.color and w.right.color):
                w.color = False;
                node = node.p;
            else:
                if(w.right.color):
                    w.left.color = True;
                    w.color = False;
                    rightRotation(tree, w);
                    w = node.p.right;
                w.color = node.p.color;
                node.p.color = True;
                w.right.color = True;
                leftRotation(tree, node.p);
                node = tree.root;
        else:
            w = node.p.left;
            if(not w.color):
                w.color = True;
                node.p.color = False;
                rightRotation(tree, node.p);
                w = node.p.left;
            if(w.left.color and w.right.color):
                w.color = False;
                node = node.p;
            else:
                if(w.left.color):
                    w.right.color = True;
                    w.color = False;
                    leftRotation(tree, w);
                    w = node.p.left;
                w.color = node.p.color;
                node.p.color = True;
                w.left.color = True;
                rightRotation(tree, node.p);
                node = tree.root;
    node.color = True;

def rbTransplant(tree, place, subtree):
    if(place.p == tree.nil):
        tree.root = subtree;
    elif(place == place.p.right):
        place.p.right = subtree;
    else:
        place.p.left = subtree;
    subtree.p = place.p;

########################################
# Visualization with graphics.py lib
########################################

def printRBTree(tree, title):
    win = GraphWin("RBTree", 700, 450);
    win.setBackground(color_rgb(3, 42, 64));

    graphTitle = Text(Point(350, 25), title)
    graphTitle.setOutline("white");
    graphTitle.draw(win);

    printNodes(win, tree, tree.root, Point(50, 0), 300);

    return win;

def printNodes(win, tree, node, pos, xOffset):
    if(node == tree.nil):
        return;

    #Drawing
    actualPos = Point(pos.x + xOffset, pos.y + 65);
    #Draw lines underneath circles first
    if(node.left != tree.nil):
        toLeft  = Line(actualPos, Point(actualPos.x-abs(xOffset/2), actualPos.y+65));
        toLeft.setOutline("white");
        toLeft.draw(win);
    if(node.right != tree.nil):
        toRight = Line(actualPos, Point(actualPos.x+abs(xOffset/2), actualPos.y+65));
        toRight.setOutline("white");
        toRight.draw(win);
    #Now draw circles
    nodeCircle = Circle(actualPos, 12);
    if(node.color):
        nodeCircle.setFill("black");
    else:
        nodeCircle.setFill(color_rgb(214, 62, 11));
    nodeCircle.setOutline("white");
    nodeText = Text(actualPos,  node.key);
    nodeText.setOutline("white");
    nodeCircle.draw(win);
    nodeText.draw(win);

    #Call for next nodes
    printNodes(win, tree, node.left, actualPos, -abs(xOffset/2));
    printNodes(win, tree, node.right, actualPos, abs(xOffset/2));



########################################
# Code to make rbtree and print it
# to show functionality
########################################

#This is the correct sequence in order to get the tree in problem
data = [28, 21, 26, 14, 41, 47, 7, 23, 12, 30, 17, 38, 10, 19, 35, 16, 20, 15, 39, 3];
nodes = [];
for d in data:
    nodes.append(Node(d));

rbTree = RBTree();
for node in nodes:
    if(nodes.index(node) == len(data)/2):
        printRBTree(rbTree, "Halfway through insertion");
    rbInsert(rbTree, node);

printRBTree(rbTree, "Same sequence as in assignment");
rbDelete(rbTree, nodes[1]);
printRBTree(rbTree, "After deleting node with key 21");
rbTransplant(rbTree, nodes[3], nodes[4]);
printRBTree(rbTree, "Transplant node 41 onto node 14 (Invalid RBTree)").getKey();

