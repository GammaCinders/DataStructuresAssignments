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
        #Both constants are just 1
        a = b = level = 1;
        offset = 0;
        while(self.table[(data.hash()+offset)%10]):
            offset = (a*level) + (b*(level**2));
            level += 1;
        self.table[(data.hash()+offset)%10] = data;

    #Searches for a data object with the same value
    #not neccesarily the exact same data object
    def search(self, data) -> Data:
        a = b = level = 1;
        offset = 0;
        while(self.table[(data.hash()+offset)%10].value != data.value):
            offset = a*level + b*(level**2);
            level += 1;
        return self.table[(data.hash()+offset)%10];

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
