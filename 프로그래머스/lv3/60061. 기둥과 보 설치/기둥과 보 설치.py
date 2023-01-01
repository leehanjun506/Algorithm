# 설치된 구조물이 가능한 구조물인지 확인함수
def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0 : #설치된 것 기둥일때
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False # 아니라면 거짓
        elif stuff == 1: #설치된 것이 보일때
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n,build_frame):
    answer = []
    for frame in build_frame: #frame개수는 최대 1000
        x,y,stuff,operate = frame
        if operate == 0 : #삭제
            answer.remove([x,y,stuff]) # 일단 삭제해보고
            if not possible(answer): # 가능한구조물인지 확인
                answer.append([x,y,stuff]) # 아니면 다시 설치
        if operate == 1:
            answer.append([x,y,stuff]) # 일단 설치
            if not possible(answer): # 가능한지 확인
                answer.remove([x,y,stuff])
    return sorted(answer) # 정렬결과 반환