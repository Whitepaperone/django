from collections import defaultdict

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    checkLst = [False for i in range(V + 1)]  # 해당 노드를 들렸는지 확인하는 리스트
    stackLst = []  # DFS를 위한 스택리스트
    nodeLst = [[] for i in range(V+1)] # 연결 노드를 리스트로 받기 위함
    for i in range(E):
        a, b = map(int, input().split())
        nodeLst[a].append(b)  # 해당노드에 연결노드를 value값으로 추가

    S, G = map(int, input().split())
    result = 0
    stackLst.append(S)
    checkLst[S] = True
    while stackLst: #스택 리스트가 있는동안
        if checkLst[G]==True:
            result=1
            break

        for i in nodeLst[S]:  # 연결 노드를 들리며
            if checkLst[i] == False :  # stack에 해당 연결노드가 없고 들린적이 없다면
                S = i  # 연결노드로 이동
                checkLst[S] = True  # 해당 노드에 들렸음을 표시
                stackLst.append(S)  # stack의 top은 늘 현재 노드 위치
                break
        else:
            S = stackLst.pop()
    print(f'#{test_case} {result}')
