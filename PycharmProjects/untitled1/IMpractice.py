def aF(y, x, n):
    for i in range(-n, n + 1):
        if 0 <= y - i < N and 0 <= x - i < N:
            if mapLst[y][x - i] == 'H' or mapLst[y - i][x] == 'H':
                mapLst[y][x - i] = 'X'
                mapLst[y - i][x] = 'X'


TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    mapLst = [list(map(str, input())) for i in range(10)]

    for i in range(N):
        for j in range(N):
            # if mapLst[i][j] in ('A', 'B', 'C'):
            #      K=ord(mapLst[i][j])-ord('A')+1
            #      for k in range(1,K+1):
            #          for dr,dc in[(),(),(),()]:
            #              ...mapLst[row+dr*k][col+dc*k]
            if mapLst[i][j] == 'A':
                aF(i, j, 1)
            elif mapLst[i][j] == 'B':
                aF(i, j, 2)
            elif mapLst[i][j] == 'C':
                aF(i, j, 3)
    total = 0
    for i in mapLst:
        for j in i:
            if j == 'H':
                total += 1
    print(f'#{test_case}', total)
