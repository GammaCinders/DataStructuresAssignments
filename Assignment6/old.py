
class Node(object):
    keys = [];
    c = [];
    n = 0;
    leaf = False;

    def __init__(self, t):
        self.keys = [None]*((2*t)-1);
        self.c = [None]*(2*t);

class BTree(object):
    t = 0;
    root = None; 

    def __init__(self, t):
        self.t = t;
        root = Node(t);
        root.c = [None]*(2*t);
        root.keys = [None]*((2*t) - 1);
        root.leaf = True;
        root.n = 0;
        self.root = root;

    def insert(self, key):
        r = self.root;
        if(r.n == ((2*self.t) - 1)):
            split = Node(self.t);
            self.root = split;
            split.leaf = False;
            split.n = 0;
            split.c[0] = r;
            self.splitChild(split, 0);
            self.insertNonfull(split, key);
        else:
            self.insertNonfull(r, key);

"""
    def splitChild(self, node, i):
        z = Node(self.t);
        y = node.c[i];
        z.leaf = y.leaf;
        z.n = self.t - 1;

        self.t - 1;
        #May have to change (t - 1 above and t below)
        for j in range(1, self.t):
            z.keys[j] = y.keys[j+t];
        if(not y.leaf):
            for j in range(1, t+1):
                z.c[j] = y.c[j+1]

        pass;
"""

    def insertNonfull(self, node, key):
        i = node.n;
        if(node.leaf):
            while(i >= 0 and key < node.keys[i]):
                node.keys[i+1] = node.keys[i];
                i -= 1;
            node.keys[i+1] = key;
            node.n += 1;
        else:
            while(i >= 0 and key < node.keys[i]):
                i -= 1;
            i += 1;
            if(node.c[i].n == ((2*self.t) - 1)):
                self.splitChild(node, i);
                if(key > node.keys[i]):
                    i += 1;
            insertNonfull(node.c[i], k);

bTree = BTree(2);
bTree.insert(10);


