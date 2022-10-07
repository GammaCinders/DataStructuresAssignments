import time
import math
import unittest

########################################
# Loops implemented in Python
########################################

def loopA(n):
    startTime = time.time();
    for i in range(n):
        otherVar = math.log(number) + 3;

    return time.time() - startTime;

def loopB(n):
    startTime = time.time();
    for i in range(n):
        for j in range(n):
            otherVar = math.log(number) + 3;
    
    return time.time() - startTime;

def loopC(n):
    startTime = time.time();
    for i in range(n):
        for j in range(i):
            otherVar = math.log(number) + 3;

    return time.time() - startTime;

def loopD(n):
    startTime = time.time();
    for i in range(n):
        for j in range(i):
            if j % 2 == 0:
                otherVar = math.log(number) + 3;

    return time.time() - startTime;



########################################
# Testing Code 
# (Just printing out times)
########################################

number = 450;
n = 4000;
baseTime = loopA(10000) / 10000;


#Comparing loops comparatively to check run times
print();
print("Expected base run time (loopA) :\t", baseTime * n);  
print("Actual base run time :\t\t\t", loopA(n), "\n");

print("Expected squared run time (loopB) :\t", baseTime * (n**2));  
print("Actual squared run time :\t\t", loopB(n), "\n");

print("Expected 1/2 squared run time (loopC) :\t", baseTime * ((n**2)/2));  
print("Actual squared run time :\t\t", loopC(n), "\n");

print("Expected 3/8 squared run time (loopD) :\t", baseTime * ((3*(n**2))/8));  
print("Actual squared run time :\t\t", loopD(n), "\n");


#Comparing each loop with multiple n values
n = 1000

#loopA
for i in range(1, 4):
    print("LoopA(" + str(i) + ") :", loopA(i*n));
print();

#loopB
for i in range(1, 5):
    print("LoopB(" + str(i) + ") :", loopB(i*n));
print();

#loopC
for i in range(1, 5):
    print("LoopC(" + str(i) + ") :", loopC(i*n));
print();

#loopC
for i in range(1, 5):
    print("LoopD(" + str(i) + ") :", loopD(i*n));
print();



########################################
# Testing running time to check if 
# loop run times matche my answers to 
# question 3
########################################

class TestSpeed(unittest.TestCase):
    def test_loopA(self):
        n = 100000
        baseUnit = loopA(n) / n
        expected = n * baseUnit
        tolerance = expected * 0.10; #90% Accuracy test
        result = loopA(n)
        self.assertTrue(result > expected-tolerance and result < expected+tolerance)

    def test_loopB(self):
        n = 1000
        baseUnit = loopA(n*100) / (n*100)
        expected = (n**2) * baseUnit
        tolerance = expected * 0.10; #90% Accuracy test
        result = loopB(n)
        self.assertTrue(result > expected-tolerance and result < expected+tolerance)
    
    def test_loopC(self):
        n = 1000
        baseUnit = loopA(n*100) / (n*100)
        expected = ((n**2) / 2) * baseUnit
        tolerance = expected * 0.10; #90% Accuracy test
        result = loopC(n)
        self.assertTrue(result > expected-tolerance and result < expected+tolerance)
    
    def test_loopD(self):
        n = 1000
        baseUnit = loopA(n*100) / (n*100)
        expected = ((3 * (n**2)) / 8) * baseUnit
        tolerance = expected * 0.10; #90% Accuracy test
        result = loopD(n)
        self.assertTrue(result > expected-tolerance and result < expected+tolerance)

unittest.main();
