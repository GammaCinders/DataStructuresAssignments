from dataclasses import dataclass;
from graphics import *;
import random; 
import time;

@dataclass
class HeapObject(object):
    data: object;

    def __init__(self, data: object):
        self.data = data;
        self.left = None;
        self.right = None;

class Heap(object):
    n: int;
    size: int;
    heap: list;

    def __init__(self, n: int) -> None:
        self.n = n;
        self.heap = [None]*n;
        self.size = 0;

    def insert(self, data) -> None:
        #if full can't insert
        if(self.size == self.n):
           return;

        self.heap[self.size] = data;
        self.size += 1;

        #if root nothing else to do
        if(self.size == 1):
            return;
        self.validate(self.size);

    def setHeap(self, heap: list) -> None:
        self.heap = heap.copy();
        self.size = len(heap);
        for i in range(1, self.size+1):
            self.validate(i);

    def validate(self, i: int) -> bool:
        parentIndex = int(i / 2);
        while(self.heap[i-1] > self.heap[parentIndex-1]):
            temp = self.heap[i-1];
            self.heap[i-1] = self.heap[parentIndex-1];
            self.heap[parentIndex-1] = temp;

            i = parentIndex;
            parentIndex = int(parentIndex / 2);
            if(parentIndex == 0):
                return;

        return True;

    def print(self, title) -> GraphWin:
        win = GraphWin(title, 1400, 1000);
        win.setBackground(color_rgb(40, 40, 40));

        self.printNodes(win, 1, Point(0, 0), 700);

        return win;

    def printNodes(self, win, i, pos, offset) -> None:
        if(i >= self.size):
            return;

        actualPos = Point(pos.x + offset, pos.y + 65);

        if((2 * i) < self.size):
            #Left child line and recursive call
            leftChildOffset = -abs(offset/2);
            leftLine = Line(actualPos, Point(actualPos.x + leftChildOffset, actualPos.y + 65));
            leftLine.setOutline("white");
            leftLine.draw(win);
            self.printNodes(win, (i * 2), actualPos, leftChildOffset);

            #Right child line and recursive call
            rightChildOffset = abs(offset/2);
            rightLine = Line(actualPos, Point(actualPos.x + rightChildOffset, actualPos.y + 65));
            rightLine.setOutline("white");
            rightLine.draw(win);
            self.printNodes(win, (i * 2) + 1, actualPos, rightChildOffset);

        #Circle
        dataCircle = Circle(actualPos, 12);
        dataCircle.setOutline("white");
        dataCircle.setFill(color_rgb(50, 65, 80))
        dataCircle.draw(win);
        #Data
        dataText = Text(actualPos, self.heap[i-1]); 
        dataText.setSize(8);
        dataText.setOutline("white");
        dataText.draw(win);


########################################
# Testing speeds for insert methods 
# and list sorts
########################################

data = [];
for i in range(1, 1001):
    data.append(i);

########################################
# In ascending order
########################################

heapOneByOne = Heap(1000);
pre = time.time();
for i in data:
    heapOneByOne.insert(i); 
print(f"Ascending order OBO :\t{time.time() - pre}");

heapAtOnce = Heap(1000);
pre = time.time();
heapAtOnce.setHeap(data);
print(f"Ascending order AO :\t{time.time() - pre}");

########################################
# In descending order
########################################

data.sort(reverse=True);

heapOneByOne = Heap(1000);
pre = time.time();
for i in data:
    heapOneByOne.insert(i); 
print(f"Descending order OBO :\t{time.time() - pre}");

heapAtOnce = Heap(1000);
pre = time.time();
heapAtOnce.setHeap(data);
print(f"Descending order AO :\t{time.time() - pre}");

########################################
# In random order 
########################################

random.shuffle(data);

heapOneByOne = Heap(1000);
pre = time.time();
for i in data:
    heapOneByOne.insert(i); 
print(f"Random order OBO :\t{time.time() - pre}");

heapAtOnce = Heap(1000);
pre = time.time();
heapAtOnce.setHeap(data);
print(f"Random order AO :\t{time.time() - pre}");
