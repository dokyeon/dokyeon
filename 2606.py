from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
bfs(1)
print(visited.count(True) - 1)
