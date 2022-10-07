
class Node(object):
    keys = [];
    c = []; #TODO maybe init to something else
    n = 0;
    leaf = False;

class BTree(object):
    t = 0;
    root = nil; 

    def __init__(self, t):
        self.t = t;
        root = Node();
        root.c = [None]*(2*t);
        root.keys = [None]*((2*t) - 1);
        root.leaf = True;
        root.n = 0;
        self.root = root;

#Methods for BTree inserts
def bTreeInsert(bTree, key):
    root = bTree.root;
    if(root.n == (2*bTree.t) - 1):
        split = Node();
        bTree.root = split;
        split.leaf = False;
        split.n = 0;
        s.c[0] = r;
        bTreeSplitChild(split, 0);
        bTreeInsertNonfull(split, key);
    else:
        bTreeInsertNonfull(root, key);

def bTreeSplitChild(node, i):
    newNode = Node();
    newNodeChild = node.c[i];
    newNode.leaf = newNodeChild.leaf;
    newNode.n = 
