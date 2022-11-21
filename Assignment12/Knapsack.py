from dataclasses import dataclass;

@dataclass
class Item(object):
    weight: int;
    value: int;
    
    def __init__(self, weight: int = 0, value: int = 0):
        self.weight = weight;
        self.value = value;

    def __str__(self):
        return f"(Value:{self.value}, Weight:{self.weight})";

class House(object):
    items: list;

    def __init__(self):
        self.items = [];

    def addItem(self, weight: int, value: int):
        self.items.append(Item(weight, value));

    def findMaxValue(self, bagSize: int):
        maxValue = [[0]*(bagSize+1) for i in range(len(self.items))];

        for item in range(len(self.items)):
            for maxWeight in range(bagSize+1):
                tempMaxWeight = maxWeight;
                tempMaxValue = 0;

                # Add item to current value and weight if possible
                if (self.items[item].weight <= tempMaxWeight):
                    tempMaxWeight -= self.items[item].weight;
                    tempMaxValue += self.items[item].value;

                # Call what you have left (problem already solved)
                # Takes advantage of python having negative indexing (in first loop)
                tempMaxValue += maxValue[item-1][tempMaxWeight];

                # Add if value is greater
                if (tempMaxValue > maxValue[item-1][maxWeight]):
                    maxValue[item][maxWeight] = tempMaxValue;
                else:
                    maxValue[item][maxWeight] = maxValue[item-1][maxWeight];


        # Now find and print which items were used
        usedItems = [False]*len(self.items); 
        usedWeight = 0;
        # Go through backwards
        print(f"Max Value: {maxValue[len(self.items)-1][bagSize]}");
        print(f"Item used:");
        for item in range(len(self.items)-1, -1, -1):
            if (maxValue[item][bagSize] != maxValue[item-1][bagSize]):
                print(f"\t{self.items[item]}");
                usedItems[item] = True;
                usedWeight += self.items[item].weight;

            if (usedWeight >= bagSize):
                break;

        return usedItems;


    def __str__(self):
        out = "";
        for item in self.items:
            out += f"{item}\n";
        return out;



########################################
# Setup and output for Knapsack #1
########################################

firstSet = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)];

firstProblem = House();
for item in firstSet:
    firstProblem.addItem(item[1], item[0]);

print();
firstProblem.findMaxValue(11);



########################################
# Setup and output for Knapsack #2
########################################

secSet = [(16808, 250), (50074, 659), (8931, 273), (27545, 879), (77924, 710), 
          (64441, 166), (84493, 43), (7988, 504), (82328, 730), (78841, 613), 
          (44304, 170), (17710, 158), (29561, 934), (93100, 279), (51817, 336), 
          (99098, 827), (13513, 268), (23811, 634), (80980, 150), (36580, 822), 
          (11968, 673), (1394, 337), (25486, 746), (25229, 92), (40195, 358), 
          (35002, 154), (16709, 945), (15669, 491), (88125, 197), (9531, 904), 
          (27723, 667), (28550, 25)];

secProblem = House();
for item in secSet:
    secProblem.addItem(item[1], item[0]);

print();
secProblem.findMaxValue(10000);
print();

