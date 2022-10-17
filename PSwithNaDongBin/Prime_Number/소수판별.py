import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

# 범위가 주어지고 그 안의 모든 소수 찾을 때는 에라토스테네스의 체 사용

n = 1000 # 2부터 1000까지
array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(true) (0,1제외)

for i in range(2,int(math.sqrt(n)+1)): # 2부터 n의 제곱근까지의 모든 수 확인
    if array[i] == True: #i가 소수인 경우
        #i를 제외한 i의 모든 배수 지우기
        j = 2
        while i*j<=n:
            array[i*j] = False
            j+=1

# 모든 소수 출력
for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')