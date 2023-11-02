#1654:랜선 자르기
import sys

K, N = map(int, input().split())
arr = []

for i in range(K):
    arr.append(int(input()))


start = 1
end = max(arr)

while(start <= end):
    mid = (start+end) // 2
    count = 0

    for i in range(K):
        count += arr[i] // mid

    if count >= N:
        start = mid + 1

    else:
        end = mid - 1

print(end)
