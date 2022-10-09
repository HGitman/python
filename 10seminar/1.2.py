N = list(map(int, input().split()))
M = set()
for i in N:
    if i in M:
        print('YES')
    else:
        print('NO')
    M.add(i)
    