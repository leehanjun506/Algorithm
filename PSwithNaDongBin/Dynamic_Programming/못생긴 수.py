n = int(input())
two = 2
three = 3
five = 5
i2,i3,i5 = 1,1,1
dp = [0]*n
dp[0] = 1
for i in range(1,n):
    dp[i] = min(two,three,five)
    
    if dp[i] == two:
        i2+=1
        two = i2*2
    if dp[i] == three:
        i3+=1
        three = i3*3
    if dp[i] == five:
        i5+=1
        five = i5*5
print(dp[n-1])    
    