import sys

input = sys.stdin.readline

T = int(input())

U = 0
D = 1
F = 2
B = 3
L = 4
R = 5


class Cube:
  def __init__(self):
    self.cube = [[['w' for _ in range(3)] for _ in range(3)],
    [['y' for _ in range(3)] for _ in range(3)],
    [['r' for _ in range(3)] for _ in range(3)],
    [['o' for _ in range(3)] for _ in range(3)],
    [['g' for _ in range(3)] for _ in range(3)],
    [['b' for _ in range(3)] for _ in range(3)]]

    # self.cube = []
    # value = 1
    # for _ in range(6):
    #   face = []
    #   for _ in range(3):
    #     row = []
    #     for _ in range(3):
    #       row.append(value)
    #       value += 1
    #     face.append(row)
    #   self.cube.append(face)


  def spin(self, myn, direction):
    li = []
    now = -1
    now_li = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]

    if myn == 'U':
      now = U
      li = [(F, 0, 0), (F, 0, 1), (F, 0, 2), (L, 0, 0), (L, 0, 1), (L, 0, 2), (B, 0, 0), (B, 0, 1), (B, 0, 2), (R, 0, 0), (R, 0, 1), (R, 0, 2)]
    elif myn == 'D':
      now = D
      now_li.reverse()
      li = [(F, 2, 0), (F, 2, 1), (F, 2, 2), (R, 2, 0), (R, 2, 1), (R, 2, 2), (B, 2, 0), (B, 2, 1), (B, 2, 2), (L, 2, 0), (L, 2, 1), (L, 2, 2)]
    elif myn == 'F':
      now = F
      li = [(U, 2, 0), (U, 2, 1), (U, 2, 2), (R, 0, 0), (R, 1, 0), (R, 2, 0), (D, 2, 2), (D, 2, 1), (D, 2, 0), (L, 2, 2), (L, 1, 2), (L, 0, 2)]
    elif myn == 'B':
      now = B
      li = [(U, 0, 0), (U, 0, 1), (U, 0, 2), (L, 2, 0), (L, 1, 0), (L, 0, 0), (D, 0, 2), (D, 0, 1), (D, 0, 0),  (R, 0, 2), (R, 1, 2), (R, 2, 2)]
    elif myn == 'L':
      now = L
      li = [(U, 0, 0), (U, 1, 0), (U, 2, 0), (F, 0, 0), (F, 1, 0), (F, 2, 0), (D, 2, 0), (D, 1, 0), (D, 0, 0), (B, 2, 2), (B, 1, 2), (B, 0, 2)]
    else:
      now = R
      li = [(U, 0, 2), (U, 1, 2), (U, 2, 2), (B, 2, 0), (B, 1, 0), (B, 0, 0), (D, 2, 2), (D, 1, 2), (D, 0, 2), (F, 0, 2), (F, 1, 2), (F, 2, 2)]

    if direction == '+':
      li.reverse()
      now_li.reverse()
    

    for i in range(2):
      temp = self.cube[now][now_li[i][0]][now_li[i][1]]
      for idx in range(i+2, 8, 2):
        self.cube[now][now_li[idx-2][0]][now_li[idx-2][1]] = self.cube[now][now_li[idx][0]][now_li[idx][1]]
    
      self.cube[now][now_li[i+6][0]][now_li[i+6][1]] = temp

      

    for i in range(3):
      temp = self.cube[li[i][0]][li[i][1]][li[i][2]]
      for idx in range(i+3, 12, 3):
        self.cube[li[idx-3][0]][li[idx-3][1]][li[idx-3][2]] = self.cube[li[idx][0]][li[idx][1]][li[idx][2]]
      
      self.cube[li[i+9][0]][li[i+9][1]][li[i+9][2]] = temp

  def getcube(self, which):
    for y in range(3):
      for x in range(3):
        print(self.cube[which][y][x], end = "")
      print()


for _ in range(T):
  new_cube = Cube()

  N = int(input())

  spin_li = input().split()

  for inp in spin_li:
    new_cube.spin(inp[0], inp[1])

  
  new_cube.getcube(0)