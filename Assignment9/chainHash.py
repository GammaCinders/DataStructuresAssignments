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

