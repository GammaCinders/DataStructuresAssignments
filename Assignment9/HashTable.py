from Data import Data;
from abc import ABC, abstractmethod;

class HashTable(ABC):
    table: list;

    def __init__(self, size):
        self.table = [None]*abs(size); 

    def __str__(self):
        string = "";
        for row in range(0, len(self.table)):
            string += f"{row}:\t"
            string += f"{self.table[row]}\n" if self.table[row] else "\n";
        return string;

    @abstractmethod
    def insert(self, data: Data) -> int:
        pass;
