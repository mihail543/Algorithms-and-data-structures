def compare(a, b):
    return int(a + b) < int(b + a)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


data = open(0).read().split()

bubble_sort(data)
print(''.join(data))
