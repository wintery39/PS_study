import sys

input = sys.stdin.readline

class Tree:
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.left = None
    self.right = None
    self.below_should_update = False

N, M, K = map(int, input().split())

value_li = []

for _ in range(N):
  n = int(input())
  value_li.append(Tree(n))

next_li = value_li

while len(next_li) > 1:
  temp_li = []
  
  for idx, next in enumerate(next_li):
    if idx%2==0:
      if len(next_li) - 1 == idx:
        temp_li.append(next)
      else:
        next.parent = Tree(next.value)
        next.parent.left = next
        temp_li.append(next.parent)
    else:
      next.parent = temp_li[-1]
      next.parent.right = next
      temp_li[-1].value += next.value

  
  next_li = temp_li


def get_sum(start, end):
  sum_val = 0
  
  while start != end:
    link = value_li[start]

    for i in range(0, 100):
      if 2**(i+1) + start > end or link.parent.right == link:
        update_strange_node(link)
        sum_val += link.value
        start += 2**i
        break
      link = link.parent
        
  return sum_val

def update_strange_node(node):
    findStrange = node
    strange = False
    is_left = []
    
    while findStrange.parent != None:
      is_left.append(True if findStrange.parent.left == findStrange else False)
      findStrange = findStrange.parent
      
      if findStrange.below_should_update:
        strange = True
        break
    
    if strange:
      idx = len(is_left) - 1
      while findStrange != node:
        findStrange.below_should_update = False
        
        differ = (findStrange.value - findStrange.right.value - findStrange.left.value) // 2
        
        findStrange.left.value += differ
        findStrange.left.below_should_update = True
        
        findStrange.right.value += differ
        findStrange.right.below_should_update = True
        
        if is_left[idx]:
          findStrange = findStrange.left
        else:
          findStrange = findStrange.right
        idx -= 1
      
      update_strange_node(node)
    
def update_parent(node):
    node = node.parent
    while node != None:
      node.value = node.left.value + node.right.value
      
      node = node.parent 

def update_tree(start, end, value):
  while start != end:
    link = value_li[start]

    for i in range(0, 100):
      if 2**(i+1) + start > end or link.parent.right == link:
        update_strange_node(link)
        link.value += value * 2**i
        link.below_should_update = True
        update_parent(link)
        start += 2**i
        break
      link = link.parent

for _ in range(M+K):
  a, b, c = input().split(maxsplit=2)

  a = int(a)
  b = int(b)
  
  b -= 1

  if a==1:
    c, d = c.split()
    c = int(c)
    d = int(d)
    
    update_tree(b, c, d)
  else:
    c = int(c)
    print(get_sum(b, c))