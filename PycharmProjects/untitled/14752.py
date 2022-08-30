
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M=int(input().split())
    maxV=0
    minV=30000
    inputV=list(map(int,input().split()))
    total=0
    for i in range(N):
        for j in range(M):
            total+=inputV[i]
        if total>maxV:
            maxV=total
        elif total<minV:
            minV=total
    result=maxV-minV
    print(f'#{test_case} {result}')


    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////

