from Data import Data;
from HashTable import HashTable;

class QuadraticHashTable(HashTable):

    def insert(self, data: Data) -> int:
        #Both constants are just 1
        level = 0;
        offset = 0;
        while(self.table[(data.hash()+offset)%10001]):
            level += 1;
            offset = level**2;
        self.table[(data.hash()+offset)%10001] = data;
        return level; #collisions
