def solution(nums):
    n = len(nums)//2
    nums = list(set(nums))
    return min(n,len(nums))