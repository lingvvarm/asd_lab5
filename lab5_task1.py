n, m = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]

connected = [[] for i in range(n+1)]

for i in range(m):
    p1, p2 = [int(i) for i in input().split()]
    connected[p1].append(p2)
    connected[p2].append(p1)

INF = 1000000000

dist = [INF for i in range(n+1)]
dist[a] = 0

visited = [0 for i in range(n+1)]
p = [0 for i in range(n+1)]

q = []
q.append((0, a))

while (len(q) != 0):
    #q_iter = iter(q)
    #it = next(q_iter)
    #cost = it[0]
    #v = it[1]
    #q.remove(it)
    it = q[0]
    cost = it[0]
    v = it[1]
    q.remove(it)

    visited[v] = 1

    ns = connected[v]
    for j in range(len(ns)):
        to = ns[j]
        if (not visited[to]):
            if dist[v] + 1 < dist[to]:
                if dist[to] != INF:
                    q.remove((dist[to], to))
                dist[to] = dist[v] + 1
                p[to] = v
                q.append((dist[to], to))


if dist[b] == INF:
    print('-1')
else:
    print(dist[b])
    i = b
    path = []
    path.append(i)
    while i != a:
        i = p[i]
        path.append(i)

    print(*path[::-1])

'''
4 5
1 4
1 3
3 2
2 4
2 1
2 3
out:
2
1 2 4

4 4
2 3
2 1
2 4
4 3
1 3
out:
2
2 1 3
'''

