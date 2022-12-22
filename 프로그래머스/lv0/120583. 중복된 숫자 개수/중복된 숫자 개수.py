from bisect import bisect_left,bisect_right
def count_by_range(array,left_v,right_v):
    right_index = bisect_right(array,right_v)
    left_index = bisect_left(array,left_v)
    return right_index-left_index
def solution(array, n):
    array.sort()
    
    return count_by_range(array,n,n)