from Data import Data;
from HashTable import HashTable;

class LinearHashTable(HashTable):

    def insert(self, data: Data) -> int:
        offset = 0;
        #could run forevery
        while(self.table[(data.hash()+offset)%10001]):
            offset += 1;
        self.table[(data.hash()+offset)%10001] = data;
        return offset; #collisions
