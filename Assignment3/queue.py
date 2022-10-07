class Queue(object):
    queueStart = 0;
    queueEnd = 0; #This is the index after the last element
    queueSize = 0;

    def __init__(self, maxSize):
        #Assuming good input here
        self.queue = [None]*maxSize;

    def enqueue(self, data):
        if(self.queueSize >= len(self.queue)):
            print("Cannot enqueue, queue is already full");
            return;
        self.queue[self.queueEnd] = data;
        self.queueEnd += 1;
        self.queueEnd %= len(self.queue);
        self.queueSize += 1;

    def dequeue(self):
        if(self.queueSize < 1):
            print("Cannat dequeue, queue is already empty");
            return;
        self.queueStart += 1;
        self.queueStart %= len(self.queue);
        self.queueSize -= 1;
        return self.queue[(self.queueStart - 1) % len(self.queue)];

    def size(self):
        return self.queueSize;

    def peek(self):
        return self.queue[(self.queueEnd - 1) % len(self.queue)];

    def print(self):
        if(self.queueSize == 0):
            print("Queue is empty"); 
            return;
        for i in range(self.queueSize):
            data = self.queue[(self.queueStart + i) % len(self.queue)];
            print(data, end = " ");
        print();

queue = Queue(40);

print("\nDequeue when empty:");
queue.dequeue();

print("\nFilling size 40 queue with enqueue:");
for i in range(40):
    queue.enqueue(i+1);
queue.print();

print("\nTrying to enqueue a 41'st element to the size 40 queue:");
queue.enqueue(41);

print("\nDequeueing and printing 15 elements from queue:");
for i in range(15):
    print(queue.dequeue(), end = " ");
print();

print("\nNew queue after removal:");
queue.print();

print("\nPrinting queue size (should be 40-15=25):");
print(queue.size());


print("\nAdding 5 elements back to force wrap around");
for i in range(5):
    queue.enqueue(i+101);
queue.print();

print("\nEmptying rest of queue with dequeue:");
for i in range(queue.size()):
    print(queue.dequeue(), end = " ");
print();

print("\nPrinting the now empty queue:");
queue.print();

print("\nEnqueueing 11 new elements and printing one last time:");
for i in range(11):
    queue.enqueue(i+201);
queue.print();
print();
