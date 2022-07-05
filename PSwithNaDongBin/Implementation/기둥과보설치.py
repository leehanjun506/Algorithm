# https://programmers.co.kr/learn/courses/30/lessons/60061
def solution(n, build_frame):
    map_row = [[0]*n for _ in range(n+1)] # 보
    map_column = [[0]*n for _ in range(n+1)] # 기둥
    
    def remove_frame(frame):
        if frame[2] == 0:
            map_column[frame[0]][frame[1]] = 0
        else:
            map_row[frame[0]][frame[1]] = 0
    def make_frame(frame):
        if frame[2] == 0: # 기둥 frame[0] x frame[1] y 
            map_column[frame[0]][frame[1]] = 1
        else: # 보
            map_row[frame[0]][frame[1]] = 1
        
    for frame in build_frame:
        if frame[3] == 0: # 삭제
            remove_frame(frame) 
        else: # 설치
            make_frame(frame)
            
            
    ans = []
    for i in range(len(map_column)+1):# 기둥
        for j in range(len(map_column)):
            if map_column[i][j] == 1:
                ans+=[i,j,0]
    for i in range(len(map_row)+1): # 보
        for j in range(len(map_row)):
            if map_row[i][j] == 1:
                ans+=[i,j,1]
    print(ans)
    ans.sort()
    return ans

solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])