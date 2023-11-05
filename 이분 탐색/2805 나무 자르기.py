#2805 : 나무 자르기
N, M = map(int, input().split())
tree = list(map(int, input().split()))
#이분탐색 검색 범위 설정
start, end = 1, max(tree) 

#이분탐색 알고리즘
while start <= end: 
    mid = (start+end) // 2
    
    #벌목된 나무 총합
    count = 0
    
    for i in tree:
        if i >= mid:
            count += i - mid
    
    #벌목 높이를 이분탐색
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
