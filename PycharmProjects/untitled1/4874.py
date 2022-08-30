T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    inputLst = input().split()
    result = ''
    stackLst = []

    for i in inputLst:
        if i.isdigit():
            stackLst.append(int(i))
        elif i == '.':
            if len(stackLst) != 1:
                result = 'error'
            else:
                result = stackLst.pop()
            pass
        else:
            if len(stackLst) >= 2:
                a = stackLst.pop()
                b = stackLst.pop()
                if i == '+':
                    result = b + a
                    stackLst.append(result)
                    pass
                elif i == '-':
                    result = b - a
                    stackLst.append(result)
                    pass
                elif i == '*':
                    result = b * a
                    stackLst.append(result)
                    pass
                elif i == '/':
                    result = b // a
                    stackLst.append(result)
            else:
                result = 'error'
                break

    print(f'#{test_case}', result)
