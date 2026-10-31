#include <iostream>
#include <string>

using namespace std;

void my_swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

class MinHeap {
private:
    int heap[200005];
    int size;

    void sift_up(int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (heap[i] < heap[parent]) {
                my_swap(heap[i], heap[parent]);
                i = parent;
            } else {
                break;
            }
        }
    }

    void sift_down(int i) {
        int n = size;
        while (true) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int smallest = i;

            if (left < n && heap[left] < heap[smallest]) {
                smallest = left;
            }
            if (right < n && heap[right] < heap[smallest]) {
                smallest = right;
            }

            if (smallest != i) {
                my_swap(heap[i], heap[smallest]);
                i = smallest;
            } else {
                break;
            }
        }
    }

public:
    MinHeap() {
        size = 0;
    }

    bool is_empty() {
        return size == 0;
    }

    void clear() {
        size = 0;
    }

    void insert(int x) {
        heap[size] = x;
        sift_up(size);
        size++;
    }

    int extract() {
        int min_val = heap[0];
        int last_val = heap[size - 1];
        size--;

        if (size > 0) {
            heap[0] = last_val;
            sift_down(0);
        }
        
        return min_val;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    MinHeap heap;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        } 
        else if (command == "ADD") {
            int num;
            cin >> num;
            heap.insert(num);
        } 
        else if (command == "EXTRACT") {
            if (heap.is_empty()) {
                cout << "CANNOT\n";
            } else {
                cout << heap.extract() << "\n";
            }
        }
    }

    return 0;
}
