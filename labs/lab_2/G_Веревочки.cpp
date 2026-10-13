#include <iostream>
using namespace std;

const int MAXN = 10001;
int a[MAXN];

bool good(int x, int n, int k) {
    long long cnt = 0;
    for (int i = 0; i < n; ++i) {
        cnt += a[i] / x;
    }
    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int l = 0;
    int r = 100*100*1000+1;

    while (r - l > 1) {
        int m = (l + r) / 2;
        if (good(m, n, k)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << l << endl;
    return 0;
}
