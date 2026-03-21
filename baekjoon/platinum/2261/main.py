import sys

input = sys.stdin.readline

N = int(input())

k = 20000
now = 3

while N >= now * now:
    k = (k // 2) + k % 2
    now = now * 2 - 1

result = (k ** 2) * 2
length = 20001 // k + 3

grid_points = [[[] for _ in range(length)] for _ in range(length)]
points = []

def caculate_distance(x, y, d_x, d_y):
    return ((x - d_x) ** 2) + ((y - d_y) ** 2)

for _ in range(N):
    x, y = map(int, input().split())
    x += 10000
    y += 10000
    points.append((x, y))
    
points.sort()

for x, y in points:
    grid_points[x//k][y//k].append((x, y))

for idx_x in range(length):
    for idx_y in range(length):
        for now_idx, (now_x, now_y) in enumerate(grid_points[idx_x][idx_y]):
            for next_idx in range(now_idx+1, len(grid_points[idx_x][idx_y])):
                next_x, next_y = grid_points[idx_x][idx_y][next_idx]
                
                if caculate_distance(now_x, 0, next_x, 0) >= result:
                    break
                
                result = min(result, caculate_distance(now_x, now_y, next_x, next_y))
                
            
            for next_x, next_y in grid_points[idx_x][idx_y+1]:
                result = min(result, caculate_distance(now_x, now_y, next_x, next_y))
            
            for next_x, next_y in grid_points[idx_x+1][idx_y+1]:
                if caculate_distance(now_x, 0, next_x, 0) >= result:
                    break
                
                result = min(result, caculate_distance(now_x, now_y, next_x, next_y))
            
            for next_x, next_y in grid_points[idx_x+1][idx_y]:
                if caculate_distance(now_x, 0, next_x, 0) >= result:
                    break
                
                result = min(result, caculate_distance(now_x, now_y, next_x, next_y))

            if idx_y > 0:
                for next_x, next_y in grid_points[idx_x+1][idx_y-1]:
                    if caculate_distance(now_x, 0, next_x, 0) >= result:
                        break
                
                    result = min(result, caculate_distance(now_x, now_y, next_x, next_y))
    

print(result)
