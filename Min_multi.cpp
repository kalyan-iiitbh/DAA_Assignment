#include <bits/stdc++.h>
using namespace std;                            
int MatrixChainOrder(int p[], int i, int j)  // Matrix Ai has dimension p[i-1] x p[i]
                                             
{                                            // for i = 1..n
	if (i == j)
		return 0;
	int k;
	int min = INT_MAX;
	int count;

		for (k = i; k < j; k++)                    	// place parenthesis at different places
{                                                   // between first and last matrix, recursively
		count = MatrixChainOrder(p, i, k)         	// calculate count of multiplications for   
				+ MatrixChainOrder(p, k + 1, j)     // each parenthesis placement and return the
				+ p[i - 1] * p[k] * p[j];           // minimum count
            if (count < min)
			min = count;
	}

	               
	return min;                            // Return minimum count
}

int main()
{
	int arr[] = { 12,21,65,18,24,93,121,16,41,31,47,5,47,29,76,18,72,15 };
	int n = sizeof(arr) / sizeof(arr[0]);

	cout << "Minimum number of multiplications is "
		<< MatrixChainOrder(arr, 1, n - 1);
}
