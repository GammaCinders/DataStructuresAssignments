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

    def findMaxValue(self, bagSize: int):
        maxValue = [[0]*len(self.items) for i in range(bagSize+1)];

        for item in range(len(self.items)):
            for maxWeight in range(bagSize+1):
                tempMaxWeight = maxWeight;
                tempMaxValue = 0;

                # Add item to current value and weight if possible
                if (self.items[item].weight <= tempMaxWeight):
                    print(self.items[item].weight);
                    print(tempMaxWeight);
                    tempMaxWeight -= self.items[item].weight;
                    tempMaxValue += self.items[item].value;

                # Call what you have left (problem already solved
                # TODO assumes no item weighs 0
                if (tempMaxWeight > 0 and item > 0):
                    tempMaxValue += maxValue[tempMaxWeight][item-1];

                # Add if value is greater
                if (tempMaxValue > maxValue[maxWeight][item]):
                    maxValue[maxWeight][item] = tempMaxValue;

        return maxValue;


    def __str__(self):
        out = "";
        for item in self.items:
            out += f"{item}\n";
        return out;



firstSet = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)];

house = House();
for item in firstSet:
    house.addItem(item[1], item[0]);

maxValues = house.findMaxValue(11);
for row in maxValues:
    print(row);



