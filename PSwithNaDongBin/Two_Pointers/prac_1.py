n = 5 # 데이터의 개수
m = 5 # 찾고자 하는 부분합
data = [1,2,3,2,5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start 차례대로 증가
for start in range(n):
    while interval_sum<m or end<n:
        interval_sum+=data[end]
        end+=1
    if interval_sum == m:
        count+=1
    interval_sum -= data[start]
print(count)