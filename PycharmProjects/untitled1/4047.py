
TC = int(input())
for tc in range(1, TC + 1):
    S = [i for i in range(1, 14)]
    D = [i for i in range(1, 14)]
    H = [i for i in range(1, 14)]
    C = [i for i in range(1, 14)]
    cardLst = input()
    deck = []
    result = 0
    for i in range(0, len(cardLst), 3):
        card = cardLst[i:i + 3]
        if card in deck:
            result = 'ERROR'
        else:
            deck.append(card)
    if result != 'ERROR':
        for i in deck:
            a = i[0]
            print(a)
            if a == 'S':
                S.pop()
            elif a == 'D':
                D.pop()
            elif a == 'H':
                H.pop()
            elif a == 'C':
                C.pop()
        result=f'{len(S)} {len(D)} {len(H)} {len(C)}'
    print(f'#{tc}', result)
