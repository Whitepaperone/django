TC = int(input())
for tc in range(1, TC + 1):
    N=int(input())
    arr=[list(map(int,input().split()))for row in range(N)]
    arr90=[[0]*N for i in range(N)]
    arr180=[[0]*N for i in range(N)]
    arr270=[[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr90[i][j]=arr[N-1-j][i]

    for i in range(N):
        for j in range(N):
            arr180[i][j]=arr90[N-1-j][i]

    for i in range(N):
        for j in range(N):
            arr270[i][j]=arr180[N-1-j][i]

    print(f'#{tc} ')
    for i in range(N):
        for a in range(N):
            print(arr90[i][a], end='')
        print(end=' ')
        for b in range(N):
            print(arr180[i][b], end='')
        print(end=' ')
        for c in range(N):
            print(arr270[i][c], end='')
        print()