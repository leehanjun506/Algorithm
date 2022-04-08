import sys
n = int(sys.stdin.readline())

list = []
for i in range(n):
    command = sys.stdin.readline()
    if 'push' in command:
        list.append(int(command.replace('push ','')))
    if 'pop' in command:
        if len(list) == 0:
            print(-1)
        else :
            print(list.pop())
    if 'size' in command:
        print(len(list))
    if 'empty' in command:
        if len(list) == 0:
            print(1)
        else :
            print(0)
    if 'top' in command:
        if len(list) == 0:
            print(-1)
        else :
            print(list[-1])
        