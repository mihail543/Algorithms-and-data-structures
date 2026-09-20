#include <iostream>
using namespace std;

void SelectionSort(int* A, int n) {
    for (int i = 0; i < n - 1; ++i) {
        int maxIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (A[j] > A[maxIndex]) {
                maxIndex = j;
            }
        }
        if (maxIndex != i) {
            int temp = A[i];
            A[i] = A[maxIndex];
            A[maxIndex] = temp;
        }
    }
}

int main() {
    int capacity = 10;
    int* arr = new int[capacity];
    int n = 0;
    int x;

    while (cin >> x) {
        if (n == capacity) {
            capacity *= 2;
            int* newArr = new int[capacity];
            for (int i = 0; i < n; ++i) {
                newArr[i] = arr[i];
            }
            arr = NULL;
            arr = newArr;
        }
        arr[n++] = x;

        while (cin.peek() == ' ' || cin.peek() == '\t') {
            cin.get();
        }
        if (cin.peek() == '\n') {
            break;
        }
    }

    SelectionSort(arr, n);

    for (int i = 0; i < n; ++i) {
        cout << arr[i];
        if (i != n - 1) cout << ' ';
    }
    cout << endl;

    arr = NULL;
    return 0;
}
