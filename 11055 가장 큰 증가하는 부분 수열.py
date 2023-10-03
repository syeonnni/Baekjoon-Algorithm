#11055 : 가장 큰 증가하는 부분 수열
A = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(A)]
dp[0] = arr[0]

# 이중 반복문 사용하여 현재 배열의 인덱스 값과 이전 배열의 인덱스 값을 비교
for i in range(A):
    for j in range(i):
        # 만약 현재 값이 이전 값보다 크다면
        if arr[i] > arr[j]:
            # 현재 인덱스 위치에서 가장 큰 값과 이전 인덱스 위치에서 가장 큰 값+현재 값 비교
            dp[i] = max(dp[i], dp[j] + arr[i])

        # 이전 값이 현재 값보다 크거나 같다면
        else:
            # 현재 인덱스 위치에서 가장 큰 값의 합과 현재 값 비교
            dp[i] = max(dp[i], arr[i])

print(max(dp))