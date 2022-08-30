def game(left,right):
    if gameLst[left] - gameLst[right] == -1 or gameLst[left] - gameLst[right] == 2:
        return right
    else:
        return left
# i와 j영역에서 우승자의 위치를 return
def winner(i, j):
    # if 영역의 데이타가 한개일 때:
    #   return 한개의 위치
    if i==j:
        return i
    lw = winner(i, (i + j) // 2)
    rw = winner((i + j) // 2 + 1, j)
    # if lw와 rw의 우승자를 결정하여 위치를 return
    return game(lw,rw)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    gameLst = list(map(int, input().split()))
    print(f'#{tc} {winner(0,N-1)+1}')
