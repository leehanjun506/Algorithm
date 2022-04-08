x = list(map(int,input().split()))

list = [int(i) for i in input().split()]

list.sort()
print(list[x[1]-1])