def par(k, curSum):
    if curSum>10:
        return
    if k == N:
        # print(result)
        # sumV = 0
        # for i in range(N):
        #     if result[i] == 1:
        #         sumV += lst[i]
        if curSum == 10:
            for i in range(N):
                if result[i] == 1:
                    print(lst[i], end=' ')
            print()
        return
    else:
        result[k]=0
        par(k+1,curSum)

        result[k]=1
        par(k+1,curSum+lst[k])
        # for i in range(2):
        #     result[k] = i
        #     par(k + 1)

def per(k):
    if k==N:
        print(result)
        for i in range(N):
            print(lst[result[i]],end=' ')
        print()
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            result[k]=i
            per(k+1)
            visited[i]=False

lst = [i for i in range(1, 11)]
N = 10

result = [-1] * N
# par(0,0)

lst=[0,1,2]
N=3
result = [-1] * N
visited=[False]*N
per(0)