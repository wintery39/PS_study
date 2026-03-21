import sys
import heapq

input = sys.stdin.readline
INFINITY = 500 * 1000 + 1

while True:
  N, M = map(int, input().split())

  if N == 0 and M == 0:
    break

  S, D = map(int, input().split())

  roads = [[] for _ in range(N)]

  for i in range(M):
    U, V, P = map(int, input().split())

    roads[U].append((V, P, i))

  heap = [(0, S, S, set())]

  visit_li = [[INFINITY, set()] for _ in range(N)]
  road_visit_li = [False for _ in range(M)]

  while len(heap) > 0:
    cost, node, last, road_set = heapq.heappop(heap)
    
    if cost > visit_li[D][0]:
      break
    
    if node == D:
      visit_li[node][0] = cost
      visit_li[node][1] = visit_li[node][1].union(visit_li[last][1]).union(road_set)
      continue
      

    if visit_li[node][0] < cost:
      continue
    
    visit_li[node][1] = visit_li[node][1].union(visit_li[last][1]).union(road_set)

    if visit_li[node][0] == cost:
      continue
    
    visit_li[node][0] = cost

    for next, add_cost, road_num in roads[node]:
      if visit_li[next][0] < cost + add_cost:
        continue

      heapq.heappush(heap, (cost + add_cost, next, node, set([road_num])))
    
  for road_num in list(visit_li[D][1]):
    road_visit_li[road_num] = True
  
  

  heap = [(0, S)]
  visit_li = [False for _ in range(N)]
    
  while len(heap) > 0:
    cost, node = heapq.heappop(heap)

    if visit_li[node]:
      continue

    if node == D:
      print(cost)
      break

    visit_li[node] = True

    for next, add_cost, road_num in roads[node]:
      if road_visit_li[road_num] or visit_li[next]:
        continue

      heapq.heappush(heap, (cost + add_cost, next))

  else:
    print(-1)

