# 백준 10825
n = int(input())

student = []
for i in range(n):
    name,kor,eng,math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    student.append([kor,eng,math,name])

new_student = sorted(student,key=lambda x:(-x[0],x[1],-x[2],x[3]))
for i in range(n):
    print(new_student[i][3])

