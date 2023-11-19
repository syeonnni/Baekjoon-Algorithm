#2110:공유기 설치
N, C = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))

array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start+end) // 2
    current = array[0]
    count = 1

    for i in range(1, len(array)):
         if array[i] >= current+mid:
            count += 1
            current = array[i]

    if count >= C:
        start = mid+1
        result = mid

    else:
        end = mid-1

print(result)
            
