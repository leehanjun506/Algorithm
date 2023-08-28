n,m = map(int,input().split())
lecture = list(map(int,input().split()))

# 블루레이의 최소 크기를 찾는다

left = max(lecture)
right = sum(lecture)

while left<=right:
    mid = (left+right)//2
    
    cnt = 0 # 블루레이의 크기가 m일때 총 블루레이의 개수
    blue_sum = 0
    for i in range(n):
        if blue_sum+lecture[i] <= mid:
            blue_sum+=lecture[i]
        else:
            blue_sum = 0
            cnt+=1
            if lecture[i] > mid:
                cnt+=1
            else:
                blue_sum = lecture[i]
    cnt+=1
    
    if m >= cnt:
        right = mid - 1
    else:
        left = mid + 1

print(left)