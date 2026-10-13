#include <iostream>
using namespace std;

const int MAXN = 10001;
int a[MAXN];

bool good(int boxes[], int n, int k, int r) {
    int cows_count = 1;
    int last_box = boxes[0];
    for (int i = 1; i < n; ++i) {
        int box = boxes[i];
        if (box - last_box >= r) {
            ++cows_count;
            last_box = box;
        }
    }
    return cows_count >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int l = 0;
    int r = a[n - 1] - a[0] + 1;

    while (r - l > 1) {
        int m = (l + r) / 2;
        if (good(a, n, k, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << l << endl;
    return 0;
}
