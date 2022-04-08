from collections import deque
import sys
n = int(sys.stdin.readline())
x=deque()
for i in range(n):
    a=sys.stdin.readline().strip().split()
    if a[0]=='push_front':
        x.appendleft(a[1])
    elif a[0]=='push_back':
        x.append(a[1])
    elif a[0]=='pop_front':
        if len(x)==0:
            print(-1)
        else:
            print(x.popleft())
    elif a[0]=='pop_back':
        if len(x)==0:
            print(-1)
        else:
            print(x.pop())
    elif a[0]=='size':
        print(len(x))
    elif a[0]=='empty':
        if len(x)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='front':
        if len(x)==0:
            print(-1)
        else:
            print(x[0])
    elif a[0]=='back':
        if len(x)==0:
            print(-1)
        else:
            print(x[-1])