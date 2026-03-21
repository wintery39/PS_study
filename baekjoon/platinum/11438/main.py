import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

class Tree:
  def __init__(self):
    self.ancestors = None
    self.height = None
    self.root = None

tree = [Tree() for _ in range(N)]
link_li = [[] for _ in range(N)]

for _ in range(N-1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1

  link_li[a].append(b)
  link_li[b].append(a)

queue = deque()
queue.append((0, 0))
tree[0].ancestors = ()
tree[0].height = 0
tree[0].root = -1

while len(queue) > 0:
  node, height = queue.popleft()

  if (height % 20 == 0):
    ancestors = tree[node].ancestors + (node, )
  else:
    ancestors = tree[node].ancestors
  
  for idx in link_li[node]:
    if tree[idx].root is None:
      tree[idx].height = height + 1
      queue.append((idx, height+1))
      tree[idx].ancestors = ancestors
      tree[idx].root = node
      
  link_li[node] = []
M = int(input())


def findDifferentIdx(start, end, a, b):
    if start>end:
      return -1

    mid = (start + end) // 2
    
    if (tree[a].ancestors[mid] != tree[b].ancestors[mid]) and (tree[a].ancestors[mid-1] == tree[b].ancestors[mid-1]):
        return mid
    elif tree[a].ancestors[mid] != tree[b].ancestors[mid]:
        return findDifferentIdx(start, mid-1, a, b)
    else:
        return findDifferentIdx(mid+1, end, a, b)
        
for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
    
  idx = findDifferentIdx(0, min(len(tree[a].ancestors), len(tree[b].ancestors)) - 1, a, b)
  
  if idx == -1:
    if(len(tree[a].ancestors) < len(tree[b].ancestors)):
      b = tree[b].ancestors[len(tree[a].ancestors)]
    elif(len(tree[a].ancestors) > len(tree[b].ancestors)):
      a = tree[a].ancestors[len(tree[b].ancestors)]
  else:
    a = tree[a].ancestors[idx]
    b = tree[b].ancestors[idx]
  
  while(a!=b):
    if tree[a].height > tree[b].height:
      a = tree[a].root
    elif tree[a].height < tree[b].height:
      b = tree[b].root
    else:
      a = tree[a].root
      b = tree[b].root
  
  print(a+1)