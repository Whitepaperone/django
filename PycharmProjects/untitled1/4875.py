dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# 2에서 3까지 갈 수 있으면 1을 return하고 아닌면 0을 return
def dfs(curR, curC):
    # 1. 스택에 시작점을 push, 시작점 방문 표시
    visited = [[False] * N for _ in range(N)]

    s = []
    s.append((curR, curC))
    visited[curR][curC] = True

    # 2. 스택에 데이타가 있는 동안
    while s:
        curR, curC = s.pop()
        # cur point와 연결된 모든 포인트에 대하여
        for d in range(4):
            newR = curR + dr[d]
            newC = curC + dc[d]
            # new가 이동이 가능하면(선이 연결되어 있으면)
            # 방문 안했으면
            if 0 <= newR < N and 0 <= newC < N and MIRO[newR][newC] != 1 and not visited[newR][newC]:
                if MIRO[newR][newC] == 3:
                    return 1
                s.append((newR, newC))
                visited[newR][newC] = True
    return 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    MIRO = [list(map(int, input())) for _ in range(N)]
    # 2를 찾는다
    for row in range(N):
        if MIRO[row].count(2):
            curC = MIRO[row].index(2)
            curR = row
            break
        # for col in range(N):
        #     if MIRO[row][col] == 2:
        #         curR = row
        #         curC = col
        #         break
    print(f'#{tc} {dfs(curR,curC)}')
