import sys
input = sys.stdin.readline
n = int(input())

list = [0]*10001

for i in range(n):
    x = int(input())
    list[x]+=1

for i in range(1,10001):
    while(list[i]!=0):
        print(i)
        list[i]-=1