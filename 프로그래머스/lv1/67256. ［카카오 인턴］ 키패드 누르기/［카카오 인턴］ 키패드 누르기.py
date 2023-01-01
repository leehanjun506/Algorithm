def solution(numbers, hand):
    pos = {}
    pos[1] = (0,0)
    pos[2] = (0,1)
    pos[3] = (0,2)
    pos[4] = (1,0)
    pos[5] = (1,1)
    pos[6] = (1,2)
    pos[7] = (2,0)
    pos[8] = (2,1)
    pos[9] = (2,2)
    pos['*'] = (3,0)
    pos[0] = (3,1)
    pos['#'] = (3,2)
    l_pos = pos['*']
    r_pos = pos['#']
    ans = ''
    def dis(x,y):
        return abs(x[0]-y[0]) + abs(x[1]-y[1])
    for i in numbers:
        if i == 1 or i == 4 or i == 7 or i == '*':
            l_pos = pos[i]
            ans += 'L'
        elif i == 3 or i == 6 or i == 9 or i == '#':
            r_pos = pos[i]
            ans += 'R'
        else:
            if dis(r_pos,pos[i])>dis(l_pos,pos[i]):
                l_pos = pos[i]
                ans += 'L'
            elif dis(l_pos,pos[i])>dis(r_pos,pos[i]):
                r_pos = pos[i]
                ans += 'R'
            else:
                if hand == 'left':
                    l_pos = pos[i]
                    ans+='L'
                else:
                    r_pos = pos[i]
                    ans+='R'
            
    return ans

