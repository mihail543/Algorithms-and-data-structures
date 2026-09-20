import sys

def anti_quick_sort_permutation(n):
    perm = list(range(1, n + 1))
    for i in range(2, n):
        perm[i // 2], perm[i] = perm[i], perm[i // 2]
    return perm


n = int(sys.stdin.read().split()[0])
perm = anti_quick_sort_permutation(n)
print(' '.join(map(str, perm)))
