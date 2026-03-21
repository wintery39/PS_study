import sys
from collections import deque


input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())


lake = [list(input().strip()) for _ in range(R)]

visit_li = [[-1 for _ in range(C)] for _ in range(R)]

queue = deque()
duck = 1
for y in range(R):
  for x in range(C):
    if lake[y][x] == '.':
      queue.append((y, x, 0))
    elif lake[y][x] == 'L':
      queue.append((y, x, duck))
      duck += 1

result = 0
duck = 0
flag = False

while True:
  next_queue = deque()

  while len(queue) > 0:
    y, x, num = queue.popleft()

    if visit_li[y][x] >= num:
      continue

    visit_li[y][x] = num

    for add_y, add_x in directions:
      move_y = y + add_y
      move_x = x + add_x

      if move_y < 0 or move_y >= R or move_x < 0 or move_x >= C:
        continue

      if (visit_li[y][x] == 1 and visit_li[move_y][move_x] == 2) or (visit_li[y][x] == 2 and visit_li[move_y][move_x] == 1):
        flag = True
        break

      if visit_li[move_y][move_x] >= num:
        continue

      if lake[move_y][move_x] == 'X' and visit_li[move_y][move_x] == -1:
        next_queue.append((move_y, move_x, num))
      else:
        queue.append((move_y, move_x, num))

    if flag:
      break
  



  
  queue = next_queue
  if flag:
    break

  result += 1
print(result)
