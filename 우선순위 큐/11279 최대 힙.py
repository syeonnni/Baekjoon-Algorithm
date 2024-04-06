#11279 : 최대 
import sys
import heapq as hq

n = int(input())
heap = []

#기본적으로 heapq는 최소 힙을 구현하므로 최대 힙을 구현하기 위해서는 -를 붙여야한다. 
for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        hq.heappush(heap, (-x))
    else:
        try:
            print(-1 * hq.heappop(heap))
        except:
            print(0)
    
