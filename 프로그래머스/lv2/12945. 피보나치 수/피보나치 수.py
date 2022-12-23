import sys
sys.setrecursionlimit(10**7)
def solution(n):

    memo = [0]*(n+1)
    memo[1] = 1
    def fib(n):
        if n==1 or n==0:
            return memo[n]
        if memo[n] != 0:
            return memo[n]
        memo[n] = fib(n-2)+fib(n-1)
        return memo[n]%1234567
    return fib(n)