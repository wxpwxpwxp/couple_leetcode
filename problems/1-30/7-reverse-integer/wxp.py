def reverse(num):
    a = []
    for i in str(num):
        a.append(int(i))
    #a = list(map(int, a))
    #a = [int(i) for i in a]
    a.reverse()
    #b = len(a) - 1
    b = 0
    if len(a) == 1 and a[0] == '0':
        print(0)
    if '-' in a:
        print(a[len(a) - 1], end='')
        while b < len(a) - 1:
            if a[b] != 0:
                print(a[b], end='')
                b = b + 1
            else:
                b = b + 1
    else:
        while b <= len(a) - 1:
            if a[b] != '0':
                print(a[b], end='')
                b = b + 1
            else:
                b = b + 1
