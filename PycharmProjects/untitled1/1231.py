"""
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
"""


def pre(root):
    if tree[root][0] != 0:
        pre(tree[root][0])
    print(wordLst[root],end='')

    if tree[root][1] != 0:
        pre(tree[root][1])


TC = 10
for test_case in range(1, TC + 1):
    N = int(input())
    treeLst = [list(input().split()) for i in range(N)]
    wordLst = [0]
    tree = [[0, 0] for _ in range(N + 1)]
    for i in treeLst:
        wordLst.append(i.pop(1))
        temp = list(map(int, i))
        if temp[1:]:
            for j in range(1, len(temp[1:]) + 1):
                tree[temp[0]][j - 1] = temp[j]
    print(f'#{test_case}',end=' ')
    pre(1)
    print()
