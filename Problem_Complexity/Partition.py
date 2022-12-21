
########################################
# Solution code for the partition
# problem
########################################

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



########################################
# Testing code
########################################

print();

# This has a valid partition: 10 + 6 + 2 = 18 = half sum
# (this is caught in 'partitionHelper()')
partitionExists = [1, 5, 5, 4, 6, 10, 1, 2, 2];
print(f"Array = {partitionExists}")
print(f"Partition does exist: {partition(partitionExists)}");
print(f"Half sum = {sum(partitionExists)/2}");
print();

# This cannot have a partition because sum is odd, so you can't
# have 2 even integer halfs (this is caught in 'partition()')
partitionNotPossible = [32, 30, 11, 3, 49, 84];
print(f"Array = {partitionNotPossible}")
print(f"Partition does exist: {partition(partitionNotPossible)}");
print(f"Half sum = {sum(partitionNotPossible)/2}");
print();

# This could have a partition, but there is no way to get the half sum
# (this is caught in 'partitionHelper()')
partitionDoesNotExist = [20, 10, 14, 3, 7, 4];
print(f"Array = {partitionDoesNotExist}")
print(f"Partition does exist: {partition(partitionDoesNotExist)}");
print(f"Half sum = {sum(partitionDoesNotExist)/2}");
print();