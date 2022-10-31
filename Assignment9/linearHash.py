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
        offset = 0;
        #could run forevery
        while(self.table[(data.hash()+offset)%10]):
            offset += 1;
        self.table[(data.hash()+offset)%10] = data;
        return offset; #collisions

    #Searches for a data object with the same value
    #not neccesarily the exact same data object
    def search(self, data) -> Data:
        #Do at most one full rotation
        for i in range(data.hash(), data.hash()+len(self.table)):
            searchData = self.table[i%10];
            if(not searchData):
                return;
            elif(searchData.value == data.value):
                return searchData;
        return None;

    def __str__(self):
        string = "";
        for row in range(0, len(self.table)):
            string += f"{row}:\t"
            string += f"{self.table[row]}\n" if self.table[row] else "\n";
        return string;
