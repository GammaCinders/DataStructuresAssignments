########################################
# Single link list node class and 
# methods (insert and print)
########################################

class SingleNode(object):
    nextNode = None;
    def __init__(self, data):
        self.data = data;

def insertNode(head, data):
    newNode = SingleNode(data);
    newNode.nextNode = head.nextNode;
    head.nextNode = newNode;

def printLL(head):
    while(head.nextNode != None):
        head = head.nextNode;
        print(head.data, end = " ");
    print("\n");



########################################
# Double link list node class and 
# insert (can reuse same printLL)
########################################

class DoubleNode(object):
    nextNode = None;
    prevNode = None;
    def __init__(self, data):
        self.data = data;

def insertDNode(head, data):
    newNode = DoubleNode(data);
    newNode.prevNode = head;
    newNode.nextNode = head.nextNode;
    if(newNode.nextNode != None):
        (newNode.nextNode).prevNode = newNode;
    head.nextNode = newNode;



########################################
# Creating SLL and swapping nodes with 
# data of 9 and 11
########################################

data = [3, 5, 7, 9, 11, 13];

#Setting up SLL
head = SingleNode(0);
print("\nSingle Link List before swap:");
for i in reversed(data):
    insertNode(head, i);
printLL(head);

#Setting up pointers for swapping SLL nodes
beforeNine = head;
while((beforeNine.nextNode).data != 9):
    beforeNine = beforeNine.nextNode;
nine = beforeNine.nextNode;
eleven = nine.nextNode;

#Now Swapping SLL nodes 9 and eleven
nine.nextNode= eleven.nextNode;
beforeNine.nextNode = eleven;
eleven.nextNode = nine;

print("Single Link List after swap:");
printLL(head);
print();



########################################
# Creating DLL and swapping nodes with 
# data of 9 and 11
########################################

#Setting up DLL
dHead = DoubleNode(0);
print("Double Link List before swap:");
for dataValues in reversed(data):
    insertDNode(dHead, dataValues);
printLL(dHead);

#Setting up pointers for swapping DLL nodes
dNine = dHead;
while(dNine.data != 9):
    dNine = dNine.nextNode;
dEleven = dNine.nextNode;

#Now Swapping DLL nodes 9 and eleven
#First setup nextNode values
(dNine.prevNode).nextNode = dEleven;
dNine.nextNode = dEleven.nextNode;
dEleven.nextNode = dNine;
#Now fix prevNode values
prevFixer = (dNine.prevNode);
while(prevFixer.nextNode != None): 
    (prevFixer.nextNode).prevNode = prevFixer;
    prevFixer = prevFixer.nextNode;

print("Double Link List after swap:");
printLL(dHead);
print();

