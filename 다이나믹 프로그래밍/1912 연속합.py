#1912 연속합
n = int(input())
data  = list(map(int, input().split()))
dp = [0]*n
dp[0] = data[0]

for i in range(n):
    dp[i] = max(dp[i-1]+data[i], data[i])

print(max(dp))
    




