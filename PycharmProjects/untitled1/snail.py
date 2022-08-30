
lst = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
curR, curC = 0, 0
N = 5


def selection(value):
    minV = 10000000000
    for row in range(N):
        for col in range(N):
            if value < lst[row][col] < minV:
                minV = lst[row][col]
                resultR, resultC = row, col
    # resultR, resultC = 0, 0
    return resultR, resultC


# 오,아,왼,위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
check = [[False] * N for i in range(N)]
d = 0
value = 0
for i in range(N * N):
    (idxR, idxC) = selection(value)
    value = lst[idxR][idxC]
    lst[curR][curC], lst[idxR][idxC] = lst[idxR][idxC], lst[curR][curC]
    check[curR][curC] = True
    newR = curR + dr[d]
    newC = curC + dc[d]

    if newR < 0 or newR >= N or newC < 0 or newC >= N or check[newR][newC]:
        d = (d + 1) % 4

    curR = curR + dr[d]
    curC = curC + dc[d]

print(lst)