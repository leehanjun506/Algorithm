def solution(answers):
    l = len(answers)
    answer = [0,0,0]
    m1 = []
    m2 = []
    m3 = []
    m_2 = [2,1,2,3,2,4,2,5]
    m_3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(l):
        m1.append((i%5)+1)
        m2.append(m_2[i%len(m_2)])
        m3.append(m_3[i%len(m_3)])
    for i in range(len(answers)):
        if answers[i] == m1[i]:
            answer[0]+=1
        if answers[i] == m2[i]:
            answer[1]+=1
        if answers[i] == m3[i]:
            answer[2]+=1
    max_ans = max(answer)
    ans = []
    for i,v in enumerate(answer):
        if v == max_ans:
            ans.append(i+1)
    return ans