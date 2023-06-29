#given an adjacency matrix find the bfs traversal pf the graph

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
# visit starting node
visit[0] = 1
# push the starting node into the stack
q.append(0)

def bfs():
    while q:
        e = q.popleft()
        output.append(e)
        for i in range(n):
            if graph[e][i] == 1 and visit.get(i) == - 1:
                visit[i] = 1
                q.append(i)
bfs()
for i in range(n):
    if visit[i] == -1:
        # unvisited even after bfs
        visit[i] = 1
        q.append(i)
        bfs()
print(output)
# lets say we start from node A




