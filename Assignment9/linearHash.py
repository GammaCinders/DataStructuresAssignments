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

    def insert(self, data: Data):
        #Do at most one full rotation (if full can't insert)
        for i in range(data.hash(), data.hash()+len(self.table)):
            if(not self.table[i%10]):
                self.table[i%10] = data;
                return;

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

data = [4371, 1323, 6173, 4199, 4344, 9679, 1989];

ht = HashTable();
for i in data:
    ht.insert(Data(i));

print(ht);
