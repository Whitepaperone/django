
def per(k,curV):

    global minV
    if curV>minV:
        return
    if k==N:
        if minV>curV:
            minV=curV
        # sumV=0
        # for row in range(N):
        #     col=result[row]
        #     sumV+=inputLst[row][col]
        # if minV>sumV:
        #     minV=sumV
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            result[k]=i
            per(k+1,curV+inputLst[k][i])
            visited[i]=False


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    inputLst=[list(map(int,input().split())) for _ in range(N)]
    result = [-1] * N
    visited=[False]*N
    minV=1e10
    per(0,0)
    print(f'#{tc} {minV}')