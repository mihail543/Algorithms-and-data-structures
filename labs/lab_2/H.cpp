#include <iostream>
using namespace std;

bool good(long long x, long long w, long long h, long long n) {
    long long a = x / w;
    long long b = x / h;
    if (a == 0 || b == 0) return false;
    if (a >= n || b >= n) return true;
    return a * b >= n;
}

int main() {
    long long w, h, n;
    cin >> w >> h >> n;

    long long l = 0;
    long long r = n * (w > h ? w : h);

    while (r - l > 1) {
        long long m = (l + r) / 2;
        if (good(m, w, h, n)) {
            r = m;
        } else {
            l = m;
        }
    }

    cout << r << endl;
    return 0;
}
