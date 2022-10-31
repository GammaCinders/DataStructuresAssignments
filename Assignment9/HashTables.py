from Data import Data;
from HashTable import HashTable;

class ChainHashTable(HashTable):

    def insert(self, data: Data) -> int:
        if(not self.table[data.hash()]):
            self.table[data.hash()] = data;
            return 0;
        else:
            temp = self.table[data.hash()];
            collisions = 1;
            while(temp.nextData):
                temp = temp.nextData;
                collisions += 1;
            temp.nextData = data;
            return collisions;

    def __str__(self):
        string = "";
        for row in range(0, len(self.table)):
            string += f"{row}:\t";
            data = self.table[row];
            while(data):
                string += f"{data.value} -> ";
                data = data.nextData;
            string += "\n";

        return string;


class LinearHashTable(HashTable):

    def insert(self, data: Data) -> int:
        offset = 0;
        while(self.table[(data.hash()+offset)%(len(self.table))]):
            offset += 1;
        self.table[(data.hash()+offset)%(len(self.table))] = data;
        return offset; #collisions


class QuadraticHashTable(HashTable):

    def insert(self, data: Data) -> int:
        level = 0;
        offset = 0;
        while(self.table[(data.hash()+offset)%(len(self.table))]):
            level += 1;
            offset = level**2;
        self.table[(data.hash()+offset)%(len(self.table))] = data;
        return level; #collisions


class SecondaryHashTable(HashTable):

    def insert(self, data: Data) -> int:
        level = 0;
        offset = 0;
        while(self.table[(data.hash()+offset)%(len(self.table))]):
            level += 1;
            offset = data.secondaryHash(level);
        self.table[(data.hash()+offset)%(len(self.table))] = data;
        return level;

