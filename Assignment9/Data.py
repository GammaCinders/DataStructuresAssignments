from dataclasses import dataclass;

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

