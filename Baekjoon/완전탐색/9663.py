#백준 9663 백트랙킹

n = int(input())

queen = [0]*n # i번 째 값이 j라면 i+1행 j+1행에 queen있는것

cnt=0

def possible(depth):
    for i in range(depth):
        if queen[depth] == queen[i] or abs(queen[depth]-queen[i]) == abs(depth-i):
            return False
    return True
        
    
    
def dfs(depth):
    global cnt
    if depth == n:
        cnt+=1
        return
    
    for i in range(n):
        queen[depth] = i
        if possible(depth):
            dfs(depth+1)


dfs(0)
print(cnt)