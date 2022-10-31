from Data import Data;
from HashTable import HashTable;

class SecondaryHashTable(HashTable):

    def insert(self, data: Data) -> int:
        level = 0;
        offset = 0;
        while(self.table[(data.hash()+offset)%10001]):
            level += 1;
            offset = data.secondaryHash(level);
        self.table[(data.hash()+offset)%10001] = data;
        return level;
