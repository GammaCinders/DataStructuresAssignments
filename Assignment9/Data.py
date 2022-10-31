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

    def secondaryHash(self, level) -> int:
        return 9973 - (level % 9973);

    def __str__(self):
        return str(self.value);

