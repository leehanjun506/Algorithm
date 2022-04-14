# 스택 예제
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) # a:b:c a부터b까지 c 간격으로 배열 만들어라(c가 음수면 역순)
stack.reverse()
print(stack)

#큐 예제
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
print(list(queue))
queue.reverse()
print(queue)

#재귀 함수
'''
def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()
recursive_function()
'''

#재귀 함수 종료 예제
'''
def recursive_function(i):
    # 100번째출력시 종료
    if i == 100:
        return
    print(f'{i}번째 재귀 함수에서 {i+1}번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(f'{i}번째 재귀 함수를 종료합니다')
    
recursive_function(1)
'''

#2가지 방식으로 구현한 팩토리얼 예제

#반복적으로 구현한 n!
def factorial_iterative(n):
    result=1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1):
        result*=i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)
    
print(f"반복적으로 '구현':{factorial_iterative(5)}")
print(f"재귀적으로 '구현':{factorial_recursive(5)}")
