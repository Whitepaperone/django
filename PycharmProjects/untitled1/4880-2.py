def tournament(first, last):
    print(first,last)
    if first == last:
        return first
    left = tournament(first, (first + last) // 2)
    right = tournament((first + last) // 2+1, last)
    return winner(left, right)

def winner(a, b):
    if what[a] - what[b] == -1 or what[a] - what[b] == 2:
        return b
    else:
        return a

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    what = list(map(int, input().split()))
    print(f'#{tc} {tournament(0, N-1) + 1}')