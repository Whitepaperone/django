def myReverse(s):
    s = list(s)
    s.reverse()
    s = ''.join(s)
    return s


def myReverse2(s):
    s = list(s)
    n = len(s)
    for i in range(n // 2):
        temp = s[i]
        s[i] = s[n - 1 - i]
        s[n - 1 - i] = temp
    s = ''.join(s)
    return s


def myStrcmp(str1, str2):
    if str1 == str2:
        return 0
    if str1 < str2:
        return -1
    else:
        return 1
    return


def myStr(num):
    str = ''
    minus = False
    if num < 0:
        num = num * (-1)
        minus = True
    while num > 0:
        a = num % 10
        str = chr(a + ord('0')) + str
        num = num // 10
    if minus == True:
        return '-' + str

    return str


a = 0


def find(t, p):
    i = 0
    j = 0
    while i < N and j < M:
        if t[i] == p[j]:
            i += 1
            j += 1
            pass
        else:
            i = i - j + 1
            j = 0
    if j == M:
        return i - M
    else:
        return -1


print(myReverse('abcd'))
print(myReverse2('abcd'))

print(myStrcmp('abcd', 'b'))
print(myStrcmp('b', 'abcd'))
print(myStrcmp('abcd', 'abcd'))

print(myStr(123))
print(myStr(3214))
print(myStr(-321))

t = 'a pattern matching algorithm test algorithm'
p = 'rithm'
N = len(t)
M = len(p)
print(find(t, p))
