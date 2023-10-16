import heapq
 
INF = float("inf")
 
n, m = map(int, input().split())
 
adj_list = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj_list[a-1].append((b-1, w))
    adj_list[b-1].append((a-1, w))
 
dist = [INF] * n
visited = [False] * n
 
heap = []
 
dist[0] = 0
heapq.heappush(heap, (0, 0))
while heap:
    curr_dist, curr_vert = heapq.heappop(heap)
    if visited[curr_vert]:
        continue
    visited[curr_vert] = True
    if curr_vert == n-1:
        break
    for neighbor, weight in adj_list[curr_vert]:
        if not visited[neighbor] and dist[neighbor] > curr_dist + weight:
            dist[neighbor] = curr_dist + weight
            heapq.heappush(heap, (dist[neighbor], neighbor))
 
if visited[n-1]:
    path = []
    curr_vert = n-1
    while curr_vert != 0:
        path.append(curr_vert + 1)
        for neighbor, weight in adj_list[curr_vert]:
            if dist[curr_vert] == dist[neighbor] + weight:
                curr_vert = neighbor
                break
    path.append(1)
    print(*path[::-1])
else:
    print(-1)