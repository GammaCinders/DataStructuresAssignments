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

    def insert(self, data):
        self.heap[self.size] = data;
        self.size += 1;

        newIndex = self.size - 1;
        parentIndex = int((newIndex - 1) / 2);
        while(self.heap[newIndex] > self.heap[parentIndex]):
            temp = self.heap[newIndex];
            self.heap[newIndex] = self.heap[parentIndex];
            self.heap[parentIndex] = temp;

            newIndex = parentIndex;
            parentIndex = int((parentIndex - 1) / 2);
            if(parentIndex < 0):
                      return;

    def print(self, title):
        win = GraphWin(title, 600, 400);
        win.setBackground(color_rgb(100, 100, 100));

        self.printNodes(win, 0, Point(0, 0), 300);

        return win;

    def printNodes(self, win, i, pos, offset):
        if(self.heap[i] == None):
            return;

        #don't need height, could pass y coordinate through pos arg
        height = int(math.log(i+1, 2));
        actualPos= Point(pos.x + offset, (height+1)*30);
        text = Text(actualPos, self.heap[i]);
        text.draw(win);

        leftIndex = (2 * i) + 1;
        rightIndex = (2 * i) + 2;
        self.printNodes(win, leftIndex, actualPos, -abs(offset/2));
        self.printNodes(win, rightIndex, actualPos, abs(offset/2));


"""
        for i in range(0, self.size):
            height = int(math.log(i+1, 2));
            print(f"Height {height: 4}: {self.heap[i]}");
"""
            


heap = Heap(100);
heap.insert(100);
heap.insert(40);
heap.insert(320);
heap.insert(2);
heap.print("Test").getKey();
