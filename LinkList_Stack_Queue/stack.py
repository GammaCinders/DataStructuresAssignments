class Stack(object):
    stackIndex = 0;
    stackSize = 0;

    def __init__(self, maxSize):
        #Assuming good input here
        self.stack = [None]*maxSize;

    def push(self, data):
        #Make sure no funny index buisines occurs
        if(self.stackSize >= len(self.stack)):
            print("Cannot push, stack is already full");
            return;
        #This is to check for the special case of the first push
        if(self.stackSize > 0):
            self.stackIndex += 1;
        self.stack[self.stackIndex] = data;
        self.stackSize += 1;

    def pop(self):
        if(self.stackSize == 0):
            print("Cannot pop, stack is empty");
            return;
        self.stackSize -= 1;
        if(self.stackSize == 0):
            return self.stack[self.stackIndex];
        self.stackIndex -= 1;
        return self.stack[self.stackIndex + 1];

    #Returns current size of filled elements in stack
    def size(self):
        return self.stackSize;

    def peek(self):
        if(self.stackSize == 0):
            print("Stack is currently empty");
        return self.stack[self.stackIndex];

    def print(self):
        if(self.stackSize == 0):
            print("Stack is currently empty");
            return;
        for dataIndex in range(self.stackIndex + 1):
            print(str(self.stack[dataIndex]), end = " ");
        print();



#Supports a max of 20 things in queue
stack = Stack(20);

print("\nPopping when empty:");
stack.pop();

print("\nFilling size 20 stack with push:");
for i in range(0, 20):
    stack.push(i+1);
stack.print();

print("\nTrying to push 21'st element to the size 20 stack:");
stack.push(21);

print("\nPopping off and printing 5 elements from stack:");
for i in range(5):
    print(stack.pop(), end = " ");
print();

print("\nPrinting stack size (should be 15, started with 20, removed 5):");
print(stack.size());

print("\nEmptying rest of stack with pop");
for i in range(stack.size()):
    print(stack.pop(), end = " ");
print();

print("\nPrinting empty stack");
stack.print();

print("\nPushing 5 new elements and printing stack one last time:");
for i in range(5):
    stack.push(i+100);
stack.print();
print();
