
# This just checks if a partition is even possible
# (aka if the sum / 2 is even)
def partition(array: list) -> bool:
    target = sum(array) / 2;

    if (target % 1):
        return False;
    else:
        return partitionHelper(array, target);

# This part is recursive to check all possible combination of numbers
def partitionHelper(array: list, target: int) -> bool:
    if (target == 0):
        return True;

    for numIndex in range(len(array)):
        newArray = array.copy();
        targetDiff = newArray.pop(numIndex);
        if(partitionHelper(newArray, target-targetDiff)):
            return True;
    
    return False;

test = [1, 5, 5, 4, 6, 10, 1, 2, 2];
print(partition(test));