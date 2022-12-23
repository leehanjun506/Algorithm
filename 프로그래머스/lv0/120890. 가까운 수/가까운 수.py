def solution(array, n):
    m = 100
    answer = 0
    array.sort()
    for i in array:
        if abs(i-n)<m:
            m = abs(i-n)
            answer = i
    return answer