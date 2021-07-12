from collections import deque

N, M, V = map(int, input().split())

ch = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  ch[m1][m2] = 1
  ch[m2][m1] = 1

# 너비 우선 탐색
def BFS(v):
  visited = [v]
  queue = deque()
  queue.append(v)

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for w in range(len(ch[v])):
      if ch[v][w] == 1 and (w not in visited):
        visited.append(w)
        queue.append(w)

# 깊이 우선 탐색
def DFS(v, visited=[]):
  visited.append(v)
  print(v, end=' ')

  for w in range(len(ch[v])):
    if ch[v][w] == 1 and (w not in visited):
      DFS(w, visited)

DFS(V)
print()
BFS(V)