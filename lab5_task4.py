from collections import deque


class edge:
    def __init__(self, to, dist):
        self.to = to
        self.dist = dist

q = deque()
n, m, s, d = [int(i) for i in input().split()]
dist = [-1 for i in range(n+1)]
graph = [[] for i in range(n+1)]

def bfs():
    global graph, dist, q
    while len(q) != 0:
        f = q[0]
        q.popleft()
        
        for i in range(len(graph[f])):
            to = graph[f][i].to
            w = graph[f][i].dist

            if dist[to] == -1 or dist[to] > dist[f] + w:
                dist[to] = dist[f] + w

                if w == 0:
                    q.appendleft(to)
                else:
                    q.append(to)



for i in range(m):
    a, b, w = [int(i) for i in input().split()]
    graph[a].append(edge(b, w))
    graph[b].append(edge(a, w))

q.appendleft(s)
dist[s] = 0
bfs()
print(dist[d])

'''
5 5 1 3
1 2 0
2 3 1
3 4 0
4 5 1
1 5 1
out: 1
'''