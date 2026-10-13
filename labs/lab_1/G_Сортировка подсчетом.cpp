#include <iostream>
using namespace std;

void counting_sort(int* arr, int n) {
    if (n <= 0) return;

    int k = arr[0];
    for (int i = 1; i < n; ++i) {
        if (arr[i] > k) {
            k = arr[i];
        }
    }

    int* counter = new int[k + 1]();
    for (int i = 0; i < n; ++i) {
        counter[arr[i]]++;
    }
    int index = 0;
    for (int num = 0; num <= k; ++num) {
        for (int j = 0; j < counter[num]; ++j) {
            arr[index++] = num;
        }
    }
    delete[] counter;
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

    counting_sort(arr, n);

    for (int i = 0; i < n; ++i) {
        cout << arr[i];
        if (i != n - 1) cout << ' ';
    }
    cout << endl;

    arr = NULL;
    return 0;
}
