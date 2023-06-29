from collections import deque

n = int(input("Enter no of nodes: "))
graph = []
print("Enter the adjacency matrix: ")

for i in range(n):
    a = list(map(int, input().split(" ")))
    graph.append(a)

visit = {}

for i in range(n):
    visit[i] = -1

q = deque()
output = []

def dfs(u):
    visit[u] = 1
    output.append(u)
    for i in range(n):
        if graph[u][i] == 1 and visit.get(i) == - 1:
            dfs(i)

dfs(0)
for i in range(n):
    if visit[i] == -1:
        # unvisited even after bfs
        dfs(i)
print(output)