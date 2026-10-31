#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class MinHeap {
private:
    vector<long long> heap;

    void sift_up(int i) {
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (heap[i] < heap[parent]) {
                swap(heap[i], heap[parent]);
                i = parent;
            } else {
                break;
            }
        }
    }

    void sift_down(int i) {
        int n = heap.size();
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
                swap(heap[i], heap[smallest]);
                i = smallest;
            } else {
                break;
            }
        }
    }

public:
    void insert(long long x) {
        heap.push_back(x);
        sift_up(heap.size() - 1);
    }

    long long extract() {
        long long min_val = heap[0];
        long long last_val = heap.back();
        heap.pop_back();

        if (!heap.empty()) {
            heap[0] = last_val;
            sift_down(0);
        }
        return min_val;
    }

    int size() {
        return heap.size();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    MinHeap heap;
    
    for (int i = 0; i < n; ++i) {
        long long num;
        cin >> num;
        heap.insert(num);
    }

    long long total_intermediate_sum = 0;

    while (heap.size() > 1) {
        long long a = heap.extract();
        long long b = heap.extract();
        long long s = a + b;
        
        total_intermediate_sum += s;
        heap.insert(s);
    }

    long long cost_cents = total_intermediate_sum * 5;
    cout << cost_cents / 100 << "." << setw(2) << setfill('0') << cost_cents % 100 << "\n";

    return 0;
}
