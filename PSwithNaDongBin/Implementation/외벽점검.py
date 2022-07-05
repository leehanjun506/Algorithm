# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # result보다 큰 값으로
    
    # 0~len(weak)-1 을 시작점으로 설정
    for start in range(length):
        # 친구 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count = 1 #투입할 친구 수
            #해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1] # 2,3,4,5
            # 시작점부터 모든 취약 지점 확인
            for index in range(start,start+length): #0,1,2,3
                # 점검 위치 벗어나는 경우
                if position < weak[index]: #1,5,6,10
                    count+=1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer,count)
    if answer > len(dist):
        return -1
    return answer