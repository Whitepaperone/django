
def bfs(s, g, N):
    visited = [0] * (N + 1)
    q = []
    q.append(s)
    visited[s] = 0
    while q:
        s = q.pop(0)
        if s==g:
            return visited[g]
        for w in adjList[s]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[s] + 1
    return 0


TC = int(input())
for test_case in range(1, TC + 1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for i in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    S, G = map(int, input().split())
    print(f'#{test_case}', bfs(S, G, N))
