from dataclasses import dataclass;

@dataclass
class Data:
    value: object;
    nextData: object;

    def __init__(self, value) -> None:
        self.value = value;
        self.nextData = None;

    def hash(self):
        return self.value % 10;
    
class HashTable(object):
    table: list;

    def __init__(self):
        self.table = [None]*10;

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

    #Searches for a data object with the same value
    #not neccesarily the exact same data object
    def search(self, data):
        searchData = self.table[data.hash()];
        while(searchData):
            if(searchData.value == data.value):
                return searchData;
        return False;            

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

