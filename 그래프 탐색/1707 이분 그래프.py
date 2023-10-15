#1707 : 이분 그래프
#인접한 노드를 거쳤을 때, 다른 색깔로 칠하기
import sys
sys.setrecursionlimit(10 ** 6)

K = int(input())

for _ in range(K):
    V, E = [int(x) for x in sys.stdin.readline().split()]

    nodes = [[] for _ in range(V)]
    visited = [0] * V

    for _ in range(E):
        u, v = [int(x) for x in sys.stdin.readline().split()]
        nodes[u - 1].append(v - 1)
        nodes[v - 1].append(u - 1)


    def dfs(node_idx):
        for v in nodes[node_idx]:
            if visited[v] == 0:
                if visited[node_idx] == 1:
                    visited[v] = 2
                elif visited[node_idx] == 2:
                    visited[v] = 1
                s = dfs(v)
                if not s:
                    return False
            elif visited[node_idx] == visited[v]:
                return False
        return True

    result = True

    for i in range(0, V):
        if visited[i] == 0:
            visited[i] = 1
            result = dfs(i)
            if not result:
                break

    print("YES") if result is True else print("NO")
