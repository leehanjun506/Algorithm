#https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    ans = [] # 스테이지 별 실패율 넣을꺼  그니깐 길이는 N
    # N은 스테이지 개수
    n = len(stages) # 사람 인원수
    for i in range(1,N+1):
        count = stages.count(i)
        if n == 0:
            fail = 0
        else:
            fail = count/n
        ans.append((i,fail))
        n-=count
    ans.sort(key=lambda x:(-x[1]))
    answer=[i[0] for i in ans]
    return answer