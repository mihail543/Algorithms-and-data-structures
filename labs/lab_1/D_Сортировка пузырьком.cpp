#include <iostream>
using namespace std;


int BubbleSortSwaps(int* A, int n) {
    int swaps = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (A[j] > A[j + 1]) {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
                ++swaps;
            }
        }
    }

    return swaps;
}

int main() {
    int n;
    cin >> n;

    int* A = new int[n];
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int swaps = BubbleSortSwaps(A, n);
    cout << swaps << endl;

    return 0;
}
