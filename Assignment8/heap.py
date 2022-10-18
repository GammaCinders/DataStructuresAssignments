from dataclasses import dataclass;
from graphics import *;
import math;

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
        if(self.size == len(self.heap)):
           return;

        self.heap[self.size] = data;
        self.size += 1;

        #if root nothing else to do
        if(self.size == 1):
            return;

        newIndex = self.size;
        parentIndex = int(newIndex / 2);
        while(self.heap[newIndex-1] > self.heap[parentIndex-1]):
            temp = self.heap[newIndex-1];
            self.heap[newIndex-1] = self.heap[parentIndex-1];
            self.heap[parentIndex-1] = temp;

            newIndex = parentIndex;
            parentIndex = int(parentIndex / 2);
            if(parentIndex == 0):
                return;

    def setHeap(self, heap: list) -> None:
        self.heap = heap;
        self.size = len(heap);
        self.validate();

    def validate(self) -> bool:
        return True;

    def print(self, title) -> GraphWin:
        win = GraphWin(title, 1200, 1000);
        win.setBackground(color_rgb(40, 40, 40));

        self.printNodes(win, 1, Point(0, 0), 600);

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

#Random numbers (from Random.org, 100 integers from 1 to 250, sorted)
data = {
        1, 3, 4, 7, 8, 11, 14, 15, 18, 19, 21, 23, 26, 30, 31, 32,
        34, 42, 43, 45, 46, 50, 51, 52, 53, 54, 57, 59, 61, 62, 65,
        68, 72, 75, 76, 77, 81, 82, 84, 87, 89, 91, 93, 97, 98, 103,
        105, 106, 112, 117, 119, 124, 128, 129, 131, 132, 133, 134,
        137, 138, 142, 143, 150, 151, 153, 156, 161, 165, 166, 174, 177,
        178, 180, 181, 183, 184, 185, 187, 193, 198, 202, 203, 206, 207, 
        215, 216, 222, 223, 228, 231, 232, 238, 241, 242, 245, 246, 247, 
        248, 249, 250
}


heapOneByOne = Heap(100);
for i in data:
    heapOneByOne.insert(i); 
heapOneByOne.print("Test").getKey();

