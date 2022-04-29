# 피보나치 함수 재귀로

def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))

# 피보나치 top-down

memo = [0]*100

def fib(x):
    if x==1 or x==2:
        return 1
    
    if memo[x]!=0:
        return memo[x]

    memo[x] = fib(x-1)+fib(x-2)
    return memo[x]

print(fib(99))

# 호출되는 함수 확인
d = [0]*100

def pibo(x):
    print('f('+str(x)+')',end=' ')
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x] = pibo(x-1)+pibo(x-2)
    return d[x]
pibo(6)

# 피보나치 bottom-up

a = [0]*100

a[1]=1
a[2]=1
n=99

for i in range(3,n+1):
    a[i]=a[i-1]+a[i-2]

print(a[n])