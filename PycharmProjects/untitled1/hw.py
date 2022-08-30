T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    mazeLst = [list(map(int, input())) for i in range(N)]
    pos = []
    goal = []
    for i in range(N):
        for j in range(N):
            if mazeLst[i][j] == 3:
                pos = [i, j]
            if mazeLst[i][j] == 2:
                goal = [i, j]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    result = 0
    while mazeLst[goal[0]][goal[1]] == 2:
        x = pos[0] + dx[i % 4]
        y = pos[1] + dy[i % 4]
        i += 1
        if N <= x or x < 0 or N <= y or y < 0:
            continue
        elif mazeLst[x][y] == 0:
            pos[0] = x
            pos[1] = y
            mazeLst[x][y] = 3
            cnt+=1
        elif mazeLst[x][y] == 1:
            continue
        elif mazeLst[x][y] == 2:
            pos[0] = x
            pos[1] = y
            mazeLst[x][y] = 3
            break
        else:
            continue

    print(f'#{test_case} {cnt}')
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
