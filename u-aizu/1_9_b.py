deck = list(input())
while deck[0] != '-':
    m = int(input())
    shuffle = [int(input()) for _ in range(m)]
    for i in shuffle:
        slice = ''.join(deck[:i:])
        del deck[:i]
        deck += slice

    print(''.join(deck))
    deck = list(input())