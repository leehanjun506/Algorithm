while True:
    a = input()
    if a == '0':
        break
    while True:
        if len(a) == 1:
            print(sum(list(map(int,a))))
            break
        a = str(sum(list(map(int,a))))