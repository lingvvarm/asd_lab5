n, m = [int(i) for i in input().split()]

adj_matrix = [[0] * (n+1) for i in range(n+1)]
visited = [0 for i in range(n+1)]


def dfs(v):
    global adj_matrix, visited, counter, n
    visited[v] = 1
    counter += 1
    for i in range(1, n+1):
        if adj_matrix[v][i] == 1 and visited[i] == 0:
            dfs(i)

for i in range(m):
    a, b = [int(i) for i in input().split()]
    adj_matrix[a][b] = adj_matrix[b][a] = 1


counter = 0
dfs(1)

if counter == n:
    print("YES")
else:
    print("NO")


'''
3 2
1 2
3 2
YES

3 1
1 3
NO


5 4
1 2
5 1
3 5
4 3
YES

4 5
1 2
2 1
2 4
2 4
4 2
NO
'''








