def solution(food):
    num = []
    for i,v in enumerate(food):
        if i == 0:
            continue
        num.append(v//2)
    people = ''
    for i,v in enumerate(num):
        people+=str(i+1)*v
    re_people = people[::-1]
    
    answer = people+'0'+re_people
    return answer