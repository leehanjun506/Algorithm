count=int(input())
for i in range(count):
    test=input()
    sum_score = 0
    score = 0
    for t in test:
        if t=='O':
            score+=1
            sum_score+=score
        else:
            score=0
    print(sum_score)