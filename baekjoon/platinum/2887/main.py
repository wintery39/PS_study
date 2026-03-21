import sys
import heapq

input = sys.stdin.readline

N = int(input())

x_planets = []
y_planets = []
z_planets = []
planets = [False for _ in range(N)]
distances = [[] for _ in range(N)]

for i in range(N):
  x, y, z = map(int, input().split())

  x_planets.append((x, i))
  y_planets.append((y, i))
  z_planets.append((z, i))

x_planets.sort()
y_planets.sort()
z_planets.sort()

for i in range(N-1):
  distances[x_planets[i][1]].append((x_planets[i+1][0] - x_planets[i][0], x_planets[i+1][1]))
  distances[x_planets[i+1][1]].append((x_planets[i+1][0] - x_planets[i][0], x_planets[i][1]))
  distances[y_planets[i][1]].append((y_planets[i+1][0] - y_planets[i][0], y_planets[i+1][1]))
  distances[y_planets[i+1][1]].append((y_planets[i+1][0] - y_planets[i][0], y_planets[i][1]))
  distances[z_planets[i][1]].append((z_planets[i+1][0] - z_planets[i][0], z_planets[i+1][1]))
  distances[z_planets[i+1][1]].append((z_planets[i+1][0] - z_planets[i][0], z_planets[i][1]))
  
route = []
result = 0
cnt = 1

def pushall(li):
  for i, j in li:
    if planets[j]:
      continue
    heapq.heappush(route, (i, j))

planets[0] = True
pushall(distances[0])

while cnt != N:
  dis, target = heapq.heappop(route)

  if planets[target]:
    continue
  
  cnt += 1
  result += dis
  planets[target] = True
  pushall(distances[target])

print(result)