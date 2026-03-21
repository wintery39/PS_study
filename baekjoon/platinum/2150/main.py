import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)



V, E = map(int, input().split())

edge = [[] for _ in range(V+1)]
reversed_edge = [[] for _ in range(V+1)]

for _ in range(E):
    A, B = map(int, input().split())
    
    edge[A].append(B)
    reversed_edge[B].append(A)
    
visit_li = [False for _ in range(V+1)]
sequence = []
result = []

def dfs(node):
    visit_li[node] = True
    
    for next_node in edge[node]:
        if not visit_li[next_node]:
            dfs(next_node)
    sequence.append(node)

def reversed_dfs(node):
    visit_li[node] = True
    result[-1].append(node)
    
    for next_node in reversed_edge[node]:
        if not visit_li[next_node]:
            reversed_dfs(next_node)


for node in range(1, V+1):
    if visit_li[node]:
        continue
    
    dfs(node)
    
visit_li = [False for _ in range(V+1)]
result = []
for i in range(V-1,-1,-1):
    node = sequence[i]
    if visit_li[node]:
        continue
    
    result.append([])
    reversed_dfs(node)
    result[-1].sort()
    
result.sort()

print(len(result))

for scc in result:
    for num in scc:
        print(num, end=" ")
    print(-1)
    

