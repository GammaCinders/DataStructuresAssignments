from Data import Data;
from HashTables import ChainHashTable, LinearHashTable, QuadraticHashTable, SecondaryHashTable;
import random;

data = [];
for i in range(1, 100001):
    data.append(i);
random.shuffle(data);

chainHashTable = ChainHashTable(10001);
chainCol = 0;
for d in data[0:500]:
    chainCol += chainHashTable.insert(Data(d));

linearHashTable = LinearHashTable(10001);
linCol = 0;
for d in data[0:500]:
    linCol += linearHashTable.insert(Data(d));

quadraticHashTable = QuadraticHashTable(10001);
quadCol = 0;
for d in data[0:500]:
    quadCol += quadraticHashTable.insert(Data(d));

secondaryHashTable = SecondaryHashTable(10001);
secondCol = 0;
for d in data[0:500]:
    secondCol += secondaryHashTable.insert(Data(d));

print(f"Chain hash table collisions:\t\t\t{chainCol}");
print(f"Linear hash table collisions:\t\t\t{linCol}");
print(f"Quadratic hash table collisions:\t\t{quadCol}");
print(f"Secondary hash function table collisions:\t{secondCol}");
