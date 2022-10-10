from graphics import *;

class Node(object):
    key = [];
    c = [];
    n = 0;
    leaf = False;

    def __init__(self, t):
        self.key = [None]*((2*t) - 1);
        self.c = [None]*(2*t);

    def __str__(self):
        return self.key;

class BTree(object):
    root = None; 
    t = 0;

    def __init__(self, t):
        self.t = t;
        self.root = Node(t);
        self.root.leaf = True;
        self.root.n = 0;
        
    def splitChild(self, x, i):
        z = Node(self.t);
        y = x.c[i];
        z.leaf = y.leaf;
        z.n = self.t - 1;
        #copying key/children
        for j in range(0, self.t-1):
            z.key[j] = y.key[j+self.t];
        if(not y.leaf):
            for j in range(0, self.t):
                z.c[j] = y.c[j+self.t];
        y.n = self.t - 1;
        #shifting key/children
        for j in range(x.n, i, -1):
            x.c[j+1] = x.c[j];
        x.c[i+1] = z;
        for j in range(x.n, i, -1):
            x.key[j] = x.key[j-1];
        x.key[i] = y.key[self.t-1];
        x.n += 1;
        
    def insert(self, key):
        r = self.root; 
        if(r.n == ((2*self.t) - 1)):
            s = Node(self.t);
            self.root = s;
            s.leaf = False;
            s.n = 0;
            s.c[0] = r;
            self.splitChild(s, 0);
            self.insertNonfull(s, key);
        else:
            self.insertNonfull(r, key);

    def insertNonfull(self, x, key):
        i = x.n - 1;
        if(x.leaf):
            while(i >= 0 and key < x.key[i]):
                x.key[i+1] = x.key[i];
                i -= 1;
            x.key[i+1] = key;
            x.n += 1;
        else:
            while(i >= 0 and key < x.key[i]):
                i -= 1;
            i += 1;
            if(x.c[i].n == ((2*self.t) - 1)):
                self.splitChild(x, i);
                if(key > x.key[i]):
                    i += 1;
            self.insertNonfull(x.c[i], key);


########################################
# Cool graphical printing function
# (just a modified version of what I 
# made for assignment 5)
########################################

def printTree(tree, title):
    width = 1500;
    height = 500;
    win = GraphWin("BTree", width, height);
    win.setBackground(color_rgb(3, 42, 64));

    graphTitle = Text(Point(width/2, 20), title);
    graphTitle.setOutline("white");
    graphTitle.setSize(10);
    graphTitle.draw(win);

    printNodes(win, tree, tree.root, Point(0, 0), width/2);

    return win;

def printNodes(win, tree, node, pos, xOffset):
    actualPos = Point(pos.x + xOffset, pos.y + 65);
    childOffset = xOffset/(2*tree.t);
    #draw the square
    halfWidth = ((2*tree.t)-1)*14;
    nodeSquare = Rectangle(Point(actualPos.x - halfWidth, actualPos.y - 10), Point(actualPos.x + halfWidth, actualPos.y + 10)); 
    nodeSquare.setOutline("white");
    nodeSquare.draw(win);
    #draw data
    textOffset = tree.t - 1;
    for i in range(0, node.n):
        offset = (i-textOffset) * ((2*halfWidth)/((2*tree.t)-1));
        text = Text(Point(actualPos.x + offset, actualPos.y), node.key[i]); 
        text.setOutline("white");
        text.draw(win);

    if(node.leaf):
        return;
    else:
        for i in range((-2*tree.t)-1, (2*tree.t), childOffset):
            childOffset = i - (tree.t - 0.5); #position offset ratio
            childOffset *= nextOffset; #adjusting for width of box
            printNodes(win, tree, node.c[i], actualPos, childOffset);

########################################
# Testing and stuff
########################################

bTree = BTree(2);

for i in range(30):
    bTree.insert(i);
    win = printTree(bTree, "Fuck off");
    win.getKey();
    win.close();





