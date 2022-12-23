def solution(arr):
    n = min(arr)
    arr.remove(n)
    return [-1] if not arr else arr