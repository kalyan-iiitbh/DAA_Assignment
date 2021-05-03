#include <bits/stdc++.h>

using namespace std;
struct Item {                           // Structure for an item which stores weight and
	int value, weight;                  // corresponding value of Item

	Item(int value, int weight)        // Constructor
	{
	this->value=value;
	this->weight=weight;
	}
};

bool cmp(struct Item a, struct Item b)                // Comparison function to sort Item according to val/weight
{                                                      // ratio
	double r1 = (double)a.value / (double)a.weight;
	double r2 = (double)b.value / (double)b.weight;
	return r1 > r2;
}
                                                             // Main greedy function to solve problem
double fractionalKnapsack(int W, struct Item arr[], int n)
{

	sort(arr, arr + n, cmp);                               	// sorting Item on basis of ratio

	
	int curWeight = 0;                             // Current weight in knapsack
	double finalvalue = 0.0;                   // Result (value in Knapsack)

	for (int i = 0; i < n; i++) {        // Looping through all Items
	  if (curWeight + arr[i].weight <= W) {   	// If adding Item won't overflow, add it completely
			curWeight += arr[i].weight;
			finalvalue += arr[i].value;
		}
		else {                           // If we can't add current Item, add fractional part
			int remain = W - curWeight;
			finalvalue += arr[i].value
						* ((double)remain
							/ (double)arr[i].weight);
			break;
		}
	}
    return finalvalue;
}


int main()
{
	int W = 120; // Weight of knapsack
	Item arr[] = {{15, 20}, {30, 25}, {5, 10}, {35, 30}, {40, 25}, {17, 21}, {12, 23}, {24, 16}, {9, 24}, {7, 16}, {28, 31}, {29, 27},
{16, 28}, {3, 8}, {6, 17}, {12, 15}, {5, 7}, {9,14}, {14, 29}, {20, 24}, {14, 9}, {6, 10}, {2, 3}, {19, 24}, {20, 28}};

	int n = sizeof(arr) / sizeof(arr[0]);


	cout << "Maximum value we can obtain = "    
		<< fractionalKnapsack(W, arr, n);   	// Function call
	return 0;
}
