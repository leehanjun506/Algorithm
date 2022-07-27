#https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    ans = [] # 스테이지 별 실패율 넣을꺼  그니깐 길이는 N
    # N은 스테이지 개수
    n = len(stages) # 사람 인원수
    for i in range(1,N+1):
        arrive = 0
        fault = 0
        for j in stages:
            if i<=j:
                arrive+=1
            if i==j:
                fault+=1
            if arrive == 0:
                false_rate = 0
            else :
                false_rate = fault/arrive
        ans.append((false_rate,i))
    
    ans.sort(key=lambda x:(-x[0],x[1]))
    answer=[]
    for i in ans:
        answer.append(i[1])
    return answer