import sys
num = int(sys.stdin.readline())
list = []
for i in range(num):
    n = sys.stdin.readline().strip()
    if 'push' in n:
        val = int(n.replace('push ',''))
        list.append(val)
    
    elif n == 'pop':
        if len(list)==0:
            print(-1)
        else:
            print(list.pop(0))
    
    elif n == 'size':
        print(len(list))
        
    elif n == 'empty':
        if len(list)==0:
            print(1)
        else:
            print(0)
    
    elif n == 'front':
        if len(list)==0:
            print(-1)
        else:
            print(list[0])
    
    elif n == 'back':
        if len(list)==0:
            print(-1)
        else:
            print(list[-1])