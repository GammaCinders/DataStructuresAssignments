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

    def __str__(self):
        return str(self.value);
    
class HashTable(object):
    table: list;

    def __init__(self):
        self.table = [None]*10;

    def insert(self, data: Data) -> int:
        #Both constants are just 1
        level = 0;
        offset = 0;
        while(self.table[(data.hash()+offset)%10]):
            level += 1;
            offset = level**2;
        self.table[(data.hash()+offset)%10] = data;
        return level; #collisions

    #Searches for a data object with the same value
    #not neccesarily the exact same data object
    def search(self, data) -> Data:
        level = 1;
        offset = 0;
        while(self.table[(data.hash()+offset)%10].value != data.value):
            offset = level**2;
            level += 1;
        return self.table[(data.hash()+offset)%10];

    def __str__(self):
        string = "";
        for row in range(0, len(self.table)):
            string += f"{row}:\t"
            string += f"{self.table[row]}\n" if self.table[row] else "\n";
        return string;
