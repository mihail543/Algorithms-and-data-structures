def quick_sort(a, low=0, high=None):
    if high is None:
        high = len(a) - 1

    if low >= high:
        return

    pivot = a[(low + high) // 2]
    i, j = low, high

    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if low < j:
        quick_sort(a, low, j)
    if i < high:
        quick_sort(a, i, high)


n = int(input())
arr = []
while len(arr) < n:
    arr.extend(map(int, input().split()))

quick_sort(arr)
print(' '.join(map(str, arr)))
