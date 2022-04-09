# 리스트 
### a.append() : 추가
### a.sort(reverse=True) : 정렬(오름or내림)
### a.reverse() : 원소를 뒤집는다
### a.insert(인덱스,값) : 인덱스에 값 추가
### a.count(x) : x의 개수 반환
### a.remove(x) : x원소 제거 but 모든 중복원소 제거 x
</br>

# 튜플
### a=() , 원소 변경 x
</br>

# 딕셔너리
### a = {key,value}
### a.keys() : 모든 키 출력
### a.values() : 모든 값 출력
### a[key] : 키에 해당하는 값 출력
</br>

# 집합
### a = {1,2,3,3} -> 중복이 빠진다 
### 중복허용x, 순서x  
</br>

# 논리 연산자
### X and Y , X or Y , not X
</br>

# 기타 연산자
### X in : 여러 개의 데이터를 담는 자료형(리스트 , 문자열 등등)
### X not in : 여러 개의 데이터를 담는 자료형
</br>

# 람다
```
x = (lambda x,y: x+y)(3,6)
```
</br>

# 입출력
### 각 데이터 공백으로 구분하여 입력
```
data = list(map(int,input().split()))
```
</br>

n,m,k 를 공백으로 구분하여 입력
</br>
```
n,m,k = map(int,input().split())
```
</br>

입력 시간단축
</br>
```
import sys

data = sys.stdin.readline().rstrip() # rstrip()은 엔터 제거
```
</br>

### 출력 f-string

```
print(f"쏼라쏼라{변수}쏼라쏼라")
```
</br>

### 리스트 안의 리스트 요소 두번째는 내림차순으로
```
c = [[1,2],[3,6],[7,6],[3,5]]
c = sorted(c,key=lambda x : (x[0],-x[1]))
print(c)
```
</br>

# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능 포함
### ex)리스트와 같은 iterable 객체에서 사용
```
from itertools import permutations, combinations, product
data = ['a','b','c']

result = list(permutations(data,2)) #순열
print(result)

a = list(combinations(data,2)) #조합
print(a)

b = list(product(data,repeat=2)) #중복순열
print(b)
```
</br>

```
import heapq

def heapsort(iterable):
    h = []
    result = []
    
    # 모든 원소 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
    
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def maxheapsort(iterable):
    
    h = []
    result = []
    
    for value in iterable:
        heapq.heappush(h,-value)
        
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
```
</br>

# bisect : 이진 탐색 쉽게 구현

### bisect_left(a,x) : 정렬순서 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
### bisect_right(a,x) : 정렬순서 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
```
from bisect import bisect_left,bisect_right

a = [1,2,4,4,8]

x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

def count_by_range(a, left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 -1~3 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))
```
</br>

# collections : deque , Counter 클래스 제공
### 덱은 리스트와 다르게 앞쪽 원소 추가,제거에도 O(1)이다.

```
from collections import deque, Counter

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
```
</br>

# Counter는 등장 횟수를 세는 기능 제공
```
l = ['red','blue','red','green','blue','blue']
counter = Counter(['red','blue','red','green','blue','blue'])

print(l.count('blue'))
print(counter['blue'])
print(counter['green'])
print(counter['green'])
print(counter)
print(dict(counter))
```
</br>

# math 라이브러리는 팩토리얼, 제곱근, 최대공약수GCD 등 계산해주는 기능
```
import math

print(math.factorial(5))

print(int(math.sqrt(16)))

print(math.gcd(21,14))
#최소공배수는 3.9버전 이상에 있음

lcm = (lambda x,y: x//(math.gcd(x,y)) * y//(math.gcd(x,y)) * math.gcd(x,y))(21,14)
print(lcm)

print(math.pi)
print(math.e)
```