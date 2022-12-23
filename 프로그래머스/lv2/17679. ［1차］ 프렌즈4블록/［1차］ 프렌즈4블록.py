def solution(m, n, board):
    l = len(board)
    m = []
    answer = 0
    for i in board:
        m.append([j for j in i])

    def check(x,y):
        change = 0
        if m[x][y] == m[x][y+1] == m[x+1][y] == m[x+1][y+1] :
            v[x][y] += 1
            v[x][y+1] += 1
            v[x+1][y] += 1
            v[x+1][y+1] += 1
            return 1
        return 0

    while(True):
        tag = 0
        v = [[0]*n for _ in range(l)]
        
        for i in range(l):
            for j in range(n):
                if i>=0 and i<l-1 and j >=0 and j<n-1 and m[i][j] != '':
                    tag+=check(i,j)
                        
        if tag == 0:
            break
        for i in range(l):
            for j in range(n):
                if v[i][j] != 0:
                    answer+=1
                    m[i][j] = ''
        new_map = []
        for j in range(n):
            new = []
            count = 0
            for i in range(l-1,-1,-1):
                if m[i][j] == '':
                    count+=1
                else:
                    new.append(m[i][j])
            for i in range(count):
                new.append('')
            new_map.append(new)
        for i in range(l):
            for j in range(n):
                m[i][j] = new_map[j][-i-1]

    return answer