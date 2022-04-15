# 내 풀이
n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(k):
    a.sort()
    b.sort()
    a[0],b[n-1] = b[n-1],a[0]

result = 0
for i in a:
    result+=i
print(result)

# 답안 예시

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

#첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))