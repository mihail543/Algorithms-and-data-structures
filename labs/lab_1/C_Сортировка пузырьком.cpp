#include <iostream>
using namespace std;

void BubbleSort(int* A, int n) {
    for (int i = 0; i < n ; ++i) {
        for (int j = 0; j < n - i - 1 ; ++j){
        	if (A[j] < A[j+1]){
        		int temp = A[j];
        		A[j] = A[j+1];
        		A[j+1] = temp;
				}	
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

     BubbleSort(arr, n);

    for (int i = 0; i < n; ++i) {
        cout << arr[i];
        if (i != n - 1) cout << ' ';
    }
    cout << endl;

    arr = NULL;
    return 0;
}
