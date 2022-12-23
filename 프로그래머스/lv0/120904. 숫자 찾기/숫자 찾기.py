def solution(num, k):
    result = 1
    for i in str(num):
        if int(i) == k:
            return result
        else:
            result+=1
    return -1
