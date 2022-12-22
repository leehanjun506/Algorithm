n = input()
first = 0
end = len(n)-1

def check_palindrome(n,first,end):
    for _ in range(end-first+1//2):
        if n[first] != n[end]:
            return True # 회문아님
        first+=1
        end-=1
    return False # 회문

if check_palindrome(n,first,end) == True: # 회문이아니면 문자열이 답
    print(len(n))
elif check_palindrome(n,first,end-1) == True: # 회문이면 회문-1이 답
    print(len(n)-1)
else:
    print(-1)