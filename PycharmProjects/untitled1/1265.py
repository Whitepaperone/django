TC = int(input())
for test_case in range(1, TC + 1):
    N, P = map(int, input().split())
    temp = 1
    for i in range(P - 1):
        S = N // P
        temp *= S
        N -= S
        P -= 1
    temp *= S
    print(f'#{test_case}', temp)
