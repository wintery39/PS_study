import sys

input = sys.stdin.readline

class Tree:
    def __init__(self, value=1):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

N = int(input())

nodes = [Tree() for _ in range(N)]
now = nodes

while len(now) > 1:
    next = []
    
    for idx, node in enumerate(now):
        if idx%2==0:
            if idx == len(now) - 1:
                next.append(node)
            else:
                node.parent = Tree(node.value)
                node.parent.left = node
                next.append(node.parent)
        else:
            node.parent = next[-1]
            next[-1].right = node
            next[-1].value += node.value
    
    now = next

root = now[0]

def get_sum(idx):
    if idx < 0:
        return 0
    
    result = 0
    d = 1
    node = nodes[idx]
    
    while idx >= 0:
        if node.parent.left == node:
            result += node.value
            idx -= d
            node = nodes[idx]
            d = 1
            
            continue
        
        d *= 2
        node = node.parent
        
    return result

def update_node(idx):
    node = nodes[idx]
    
    while node:
        node.value -= 1
        node = node.parent


A = [None for _ in range(1000001)]

result = 0
cnt = 0

for idx, i in enumerate(list(map(int, input().split()))):
    A[i] = idx
    
for i in list(map(int, input().split())):
    idx = A[i]
    
    result += get_sum(idx - 1)
    
    update_node(idx)
    
    
print(result)