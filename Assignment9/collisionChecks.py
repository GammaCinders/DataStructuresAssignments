from HashTable import Data;
from HashTables import ChainHashTable, LinearHashTable, QuadraticHashTable, DoubleHashTable;
import random;

if __name__ == "__main__":

########################################
# Extra Testing
########################################

    otherData = [4371, 1323, 6173, 4199, 4344, 9679, 1989];

    print("\nChain Hash Table");
    chainHashTable = ChainHashTable(10);
    for d in otherData:
        chainHashTable.insert(Data(d));
    print(chainHashTable);

    print("Linear Hash Table");
    linearHashTable = LinearHashTable(10);
    for d in otherData:
        linearHashTable.insert(Data(d));
    print(linearHashTable);

    print("Quadratic Hash Table");
    quadraticHashTable = QuadraticHashTable(10);
    for d in otherData:
        quadraticHashTable.insert(Data(d));
    print(quadraticHashTable);

    print("Double Hash Table");
    doubleHashTable = DoubleHashTable(10);
    for d in otherData:
        doubleHashTable.insert(Data(d), 7);
    print(doubleHashTable);

########################################
# Problem 2
########################################

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

    doubleHashTable = DoubleHashTable(10001);
    doubleCol = 0;
    for d in data[0:500]:
        doubleCol += doubleHashTable.insert(Data(d), 9973);

    print();
    print(f"Chain hash table collisions:\t\t{chainCol}");
    print(f"Linear hash table collisions:\t\t{linCol}");
    print(f"Quadratic hash table collisions:\t{quadCol}");
    print(f"Double hash function table collisions:\t{doubleCol}");
    print();
