TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    CHEEZE = [0] + list(map(int, input().split()))

    PAN = [i for i in range(1,N+1)]
    M-=N
    num = 1
    result=0
    while PAN:
        if len(PAN)==1:
            result=PAN.pop()
            break
        pizza = PAN.pop(0)
        CHEEZE[pizza]=CHEEZE[pizza] // 2
        if CHEEZE[pizza] == 0:
            if num <= M:
                PAN.append(max(PAN)+1)
                M-=1
            else:
                result=CHEEZE.index(max(CHEEZE))
        else:
            PAN.append(pizza)


    print(f'#{tc}',result)
