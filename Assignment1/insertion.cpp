#include <iostream>
#include <stdio.h>

void getInput();
void sort(int array[]);
void printArray();

int input[5] = {0};

int main() {
	getInput();
	sort(input);

	return 0;
}

void getInput() {
	for(int i=0; i<5; i++) {
		printf("\nEnter number #%i : ", i+1);
		std::cin >> input[i];
		printArray();
	}
}

void sort(int array[]) {
	std::cout << "\nSorting Array Steps:\n";
	printArray();
	for(int i=1; i<5; i++) {
		int j = i;
		while(j > 0 && input[j] < input[j-1]) {
			int temp = input[j-1];
			input[j-1] = input[j];
			input[j] = temp;
			j--;
		}

		printf("Step #%d : ", i);
		printArray();
	}	
	std::cout << "\n";
}

void printArray() {
	for(int i=0; i<5; i++) {
		printf("[%d] ", input[i]);
	}

	std::cout << "\n";
}
