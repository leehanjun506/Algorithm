n = int(input())
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            a[j] = False
            
ans = 1        
for i in primes:
    prime = i
    while(True):
        if i <= n:
            i*=prime
        else:
            prev = i//prime
            ans*=prev
            ans%=987654321
            break
print(ans)