def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    answer.sort()
    
    return [-1] if not answer else answer