from graphics import *;
import string;

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
        if(r.n == (2*self.t) - 1):
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
    width = 1200;
    height = 500;
    win = GraphWin("BTree", width, height);
    win.setBackground(color_rgb(3, 42, 64));

    graphTitle = Text(Point(width/2, 20), title);
    graphTitle.setOutline("white");
    graphTitle.setSize(10);
    graphTitle.draw(win);

    printNodes(win, tree, tree.root, Point(width/2, 60), width);

    return win;

def printNodes(win, tree, node, pos, width):
    halfWidth = (node.n)*6; #this is the halfWidth for the box

    if(not node.leaf):
        #print lines and call recursive first
        #it's kinda odd order, but it works easier I think
        lineStart = -halfWidth; 
        nextWidth = width / (node.n + 1);
        childOffsetRatio = -(node.n);
        for i in range(0, node.n + 1):
            childPos = Point(pos.x + childOffsetRatio*(nextWidth/2), pos.y + 60)
            childLine = Line(Point(pos.x + lineStart, pos.y+10), Point(childPos.x, childPos.y - 10));
            childLine.setOutline("white");
            childLine.draw(win);
            lineStart += (halfWidth*2) / (node.n);
            printNodes(win, tree, node.c[i], childPos, nextWidth); 
            childOffsetRatio += 2;

    #drawing box
    rect = Rectangle(Point(pos.x - halfWidth, pos.y - 10), Point(pos.x + halfWidth, pos.y + 10)); 
    rect.setOutline("white");
    rect.draw(win);
    #drawing data
    tempKeys = [];
    for i in range(0, node.n):
        tempKeys.append(node.key[i]);
    keysText = Text(pos, tempKeys);
    keysText.setSize(10);
    keysText.setOutline("white");
    keysText.draw(win);


########################################
# Testing and stuff
########################################

bTreeTwo = BTree(2);
bTreeThree = BTree(3);

for letter in list(string.ascii_lowercase):
    bTreeTwo.insert(letter);
    bTreeThree.insert(letter);

win = printTree(bTreeTwo, "BTree with t=2");
win = printTree(bTreeThree, "BTree with t=3");
win.getKey();
win.close();
