from dataclasses import dataclass;

@dataclass
class Item(object):
    weight: int;
    value: int;
    
    def __init__(self, weight: int = 0, value: int = 0):
        self.weight = weight;
        self.value = value;

    def __str__(self):
        return f"Item: ({self.weight}, {self.value})";

class House(object):
    items: list;

    def __init__(self):
        self.items = [];

    def addItem(self, weight: int, value: int):
        self.items.append(Item(weight, value));

    def findMaxValue(self, maxWeight: int):
        maxValue = [[0]*len(self.items) for i in range(len(self.items))];

        for item in range(len(self.items)):
            for maxWeight in range(len(self.items[item])):
                # Need temp weight and value
                if (self.items[item].weight <= maxWeight):
                pass;

        # Go through each row
        # Go through each column

    def __str__(self):
        out = "";
        for item in self.items:
            out += f"{item}\n";
        return out;



firstSet = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)];

house = House();
for item in firstSet:
    house.addItem(item[0], item[1]);
house.findMaxValue(100);
print(house);
