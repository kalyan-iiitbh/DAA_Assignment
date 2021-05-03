#include <bits/stdc++.h>              // A dynamic programming based
using namespace std;                  // solution for 0-1 Knapsack problem

int max(int a, int b)               // A utility function that returns 
{                                   // maximum of two integers
	return (a > b) ? a : b;
}
int knapSack(int W, int wt[], int val[], int n)   // Returns the maximum value that
{                                                 // can be put in a knapsack of capacity W
	int i, w;
	int K[n + 1][W + 1];
    for(i = 0; i <= n; i++)                      // Build table K[][] in bottom up manner
	{
		for(w = 0; w <= W; w++)
		{
			if (i == 0 || w == 0)
				K[i][w] = 0;
			else if (wt[i - 1] <= w)
				K[i][w] = max(val[i - 1] +
								K[i - 1][w - wt[i - 1]],
								K[i - 1][w]);
			else
				K[i][w] = K[i - 1][w];
		}
	}
	return K[n][W];
}
int main()
{
	int val[] = { 20,25,10,30,25,21,23,16,24,16,31,27,28,8,17,15,7,14,29,24,9,10,3,24,28};
	int wt[] = { 15,30,5,35,40,17,12,24,9,7,28,29,16,3,6,12,5,9,14,20,14,6,2,19,20};
	int W = 120;
	int n = sizeof(val) / sizeof(val[0]);
	
	cout << knapSack(W, wt, val, n);
	
	return 0;
}
