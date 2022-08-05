import bisect

n,target = map(int,input().split())
array = list(map(int,input().split()))

left_index = bisect.bisect_left(array,target)
right_index = bisect.bisect_right(array,target)
count = right_index-left_index

if count == 0:
    print(-1)
else:
    print(count)