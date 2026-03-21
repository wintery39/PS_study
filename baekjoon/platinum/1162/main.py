import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())

roads = [[] for _ in range(N)]
visit = [-1 for _ in range(N)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    
    a -= 1
    b -= 1
    
    roads[a].append((cost, b))
    roads[b].append((cost, a))
    
heap = [(0, K, 0)] # cost, k, node

while heap:
    cost, now_k, node = heapq.heappop(heap)
    
    if visit[node] >= now_k:
        continue
    
    if node == N-1:
        print(cost)
        break
    
    visit[node] = now_k
    
    for add_cost, destination in roads[node]:
        if visit[destination] >= now_k:
            continue
        
        heapq.heappush(heap, (cost + add_cost, now_k, destination))
        
        if visit[destination] >= now_k - 1:
            continue
        
        heapq.heappush(heap, (cost, now_k - 1, destination))