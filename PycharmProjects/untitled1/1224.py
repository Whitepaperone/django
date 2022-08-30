T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    inputLst = input()
    result = ''
    stackLst = []
    icp = {'+':1, '-': 1, '*':2, '/': 2, ('('): 3}
    isp = {'+':1, '-': 1, '*':2, '/': 2,('('): 0}

    for i in inputLst:
        if i.isdigit():
            result += i
        elif i == ')':
            while stackLst and stackLst[-1] != '(':
                result += stackLst.pop()
            stackLst.pop()
        else:
            while stackLst and icp.get(i) <= isp.get(stackLst[-1]):
                result += stackLst.pop()
            stackLst.append(i)


    while stackLst:
        result += stackLst.pop()

    for i in result:
        if i.isdigit():
            stackLst.append(int(i))
        else:
            num1 = stackLst.pop()
            num2 = stackLst.pop()
            if i == '+':
                stackLst.append(num2 + num1)
            else:
                stackLst.append(num2 * num1)
    ans = stackLst.pop()

    print(f'#{test_case}', ans)
