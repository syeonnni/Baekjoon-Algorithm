#11724 : 연결 요소의 개수
#DFS 함수
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 노드의 수 선언 
count = 0 
visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        # 함수 DFS가 한 번 끝날 때마다 count에 1씩 증가
        count += 1

print(count)
