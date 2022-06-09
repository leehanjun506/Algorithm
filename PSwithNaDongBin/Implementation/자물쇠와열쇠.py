# https://programmers.co.kr/learn/courses/30/lessons/60059
def solution(key, lock):
    def rout(key):
        new_key=[[1]*len(key) for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_key[i][j] = key[len(key)-1-j][i]
        return new_key
    key1 = key
    key2 = rout(key1)
    key3 = rout(key2)
    key4 = rout(key3)
    ans = [key1,key2,key3,key4]
    map = [[2]*(len(lock)+2*len(key)) for _ in range(2*len(key)+len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock)):
            map[len(key)+i][len(key)+j]=lock[i][j]
    cnt = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                cnt+=1
    val = 0
    error = 0
    for a in range(len(key)+len(lock)):
        for b in range(len(key)+len(lock)):
            for k in ans:
                
                for i in range(len(k)):
                    for j in range(len(k)):
                        if map[a+i][b+j] != 2:
                            if k[i][j] == 1 and map[a+i][b+j] == 1:
                                error+=1
                        if k[i][j] == 1 and map[a+i][b+j] == 0:
                            val+=1
                if val == cnt and error == 0:
                    return True
                else:
                    val = 0
                    error = 0
    return False