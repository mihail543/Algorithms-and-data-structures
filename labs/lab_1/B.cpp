#include <iostream>
using namespace std;

void InsertionSort(int* A, int n) {
    for (int i = 1; i < n ; ++i) {
        int key = A[i];
        int j = i;
         while (j >= 1 && A[j-1] > key){
         	A[j] = A[j-1];
         	--j;
		 }
        A[j] = key;
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

    InsertionSort(arr, n);

    for (int i = 0; i < n; ++i) {
        cout << arr[i];
        if (i != n - 1) cout << ' ';
    }
    cout << endl;

    arr = NULL;
    return 0;
}
