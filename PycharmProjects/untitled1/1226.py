import pprint

def bfs(i, j, N):
    visited = [[0] * N for i in range(N)]

    q = []
    q.append((i, j))
    visited[i][j] = 0
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


    return 0


TC = 10
for tc in range(1, TC + 1):
    N=int(input())
    maze = [list(map(int, input())) for i in range(16)]
    M = len(maze)
    sti = -1
    stj = -1
    for i in range(M):
        for j in range(M):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    result = 0
    print(f'#{N}', bfs(sti, stj, M))
