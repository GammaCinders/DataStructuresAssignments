from dataclasses import dataclass;
from abc import ABC, abstractmethod;

@dataclass
class Data:
    value: object;
    nextData: object;

    def __init__(self, value) -> None:
        self.value = value;
        self.nextData = None;

    def hash(self) -> int:
        return self.value % 300;

    #doing params like this because it works 
    def secondaryHash(self, num) -> int:
        return num - (self.value % num);

    def __str__(self):
        return str(self.value);

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
