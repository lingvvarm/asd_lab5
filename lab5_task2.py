import queue

n, x = [int(i) for i in input().split()]
x -= 1
graph = []
distances = [-1 for i in range(n+1)]

for i in range(n):
    row = [int(i) for i in input().split()]
    graph.append(row)

q = queue.Queue()
q.put(x)
distances[x] = 0

while (q.qsize() != 0):
    v = q.queue[0]
    q.get()
    for i in range(n):
        if distances[i] == -1 and graph[v][i]:
            q.put(i)
            distances[i] = distances[v] + 1

print(*distances[:-1])



'''
3 3
0 1 1
1 0 1
1 0 0
out: 1 2 0

6 5
0 1 1 0 0 0
1 0 0 0 0 0
1 1 0 0 0 0
0 0 0 0 1 0
0 0 1 1 0 0
0 1 0 0 0 0
out: 2 2 1 1 0 -1
'''


