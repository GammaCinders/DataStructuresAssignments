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
