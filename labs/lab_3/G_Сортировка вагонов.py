n = int(input())
arr = list(map(int, input().split()))
cnt = 1
st1 = []
st2 = []
tpk = []
for i in range(n,0,-1):
    st1.append(arr[i-1])
for i in range(n):
    x = st1.pop()
    if cnt == x:
        st2.append(x)
        cnt+=1
    else:
        tpk.append(x)
    while len(tpk) > 0 and cnt == tpk[-1]:
        x = tpk.pop()
        st2.append(x)
        cnt+=1

print("YES" if len(tpk)==0 else "NO")
