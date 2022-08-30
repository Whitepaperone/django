TC=int(input())
for test_case in range(1,TC+1):
    N, M = map(int, input().split())
    nLst = list(map(int, input().split()))
    for i in range(M):
        temp=nLst.pop(0)
        nLst.append(temp)
    print(f'#{test_case} {nLst[0]}')