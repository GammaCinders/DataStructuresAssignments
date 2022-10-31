from secondaryHash import Data;

import chainHash as chain;
import linearHash as linear;
import quadraticHash as quad;
import secondaryHash as second; 



data = [4371, 1323, 6173, 4199, 4344, 9679, 1989];



chainHashTable = chain.HashTable();
chainCol = 0;
for d in data:
    chainCol += chainHashTable.insert(Data(d));

linearHashTable = linear.HashTable();
linCol = 0;
for d in data:
    linCol += linearHashTable.insert(Data(d));

quadraticHashTable = quad.HashTable();
quadCol = 0;
for d in data:
    quadCol += quadraticHashTable.insert(Data(d));

secondaryHashTable = second.HashTable();
secondCol = 0;
for d in data:
    secondCol += secondaryHashTable.insert(Data(d));

print("Chain Hash Table");
print(chainHashTable);
print("Linear Hash Table");
print(linearHashTable);
print("Quadratic Hash Table");
print(quadraticHashTable);
print("Secondary Hash Table");
print(secondaryHashTable);

"""
print(f"Chain hash table collisions:\t\t\t{chainCol}");
print(f"Linear hash table collisions:\t\t\t{linCol}");
print(f"Quadratic hash table collisions:\t\t{quadCol}");
print(f"Secondary hash function table collisions:\t{secondCol}");
"""
