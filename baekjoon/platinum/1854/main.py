import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
edge = [[] for _ in range(n+1)]
visit_li = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    
    edge[a].append((b, c))
    
heap = [(0, 1)]

while heap:
    cost, city = heapq.heappop(heap)
    
    if len(visit_li[city]) == k:
        continue
    
    # if len(visit_li[city]) != 0 and visit_li[city][-1] == cost:
    #     continue
    
    visit_li[city].append(cost)
    
    for destination, add_cost in edge[city]:
        if len(visit_li[destination]) == k:
            continue
    
        
        heapq.heappush(heap, (cost + add_cost, destination))

for i in range(1, n+1):
    result = visit_li[i]
    
    if len(result) == k:
        print(result[-1])
    else:
        print(-1)