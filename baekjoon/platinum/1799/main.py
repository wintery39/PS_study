import sys

input = sys.stdin.readline

N = int(input())

chess_pan = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, -1), (1, -1), (-1, 1), (1, 1)]


def markPan(y, x, num):  
  chess_pan[y][x] = num
  
  for add_y, add_x in dir:
    move_y = y
    move_x = x
    while True:
      move_y += add_y
      move_x += add_x

      if move_y >= N or move_y < 0 or move_x >= N or move_x < 0:
        break
  
      if chess_pan[move_y][move_x] == 1:
        chess_pan[move_y][move_x] = num
      

def erasePan(y, x, num):
  chess_pan[y][x] = 1
  
  for add_y, add_x in dir:
    move_y = y
    move_x = x
    while True:
      move_y += add_y
      move_x += add_x

      if move_y >= N or move_y < 0 or move_x >= N or move_x < 0:
        break
  
      if chess_pan[move_y][move_x] == num:
        chess_pan[move_y][move_x] = 1

    

def getResult(num, res):
  if num >= N**2:
    return res
  
  y = num // N
  
  x = num % N
  
  if N%2==0 and y%2==1:
    if x%2==0:
      x += 1
    else:
      x-= 1  
  
  result = 0

  if chess_pan[y][x] == 1:
    markPan(y, x, -num)
    result = getResult(num + 2, res + 1)
    erasePan(y, x, -num)
  
  result = max(result, getResult(num + 2, res))

  return result

print(getResult(0, 0) + getResult(1, 0))
  