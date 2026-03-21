import sys

input = sys.stdin.readline

# 1) cost 3
# 2) cost 5
# 3) cost 7

# 1 3 1 1
## 1 2 2 0

N = int(input())

A = list(map(int, input().split()))

A.append(0)
A.append(0)

result = 0

def add_result(num, cost):
    global result
    
    if num == 1:
        result += cost*3
    elif num == 2:
        result += cost*5
    else:
        result += cost*7

for i in range(N):
    if A[i] == 0:
        continue
    
    if A[i+1] > A[i+2]:
        d = A[i+1]-A[i+2]
        
        cost = min(A[i], d)
        A[i] -= cost
        A[i+1] -= cost
        
        add_result(2, cost)

    if A[i] > 0:
        min_val = min(A[i], A[i+1], A[i+2])
        
        if A[i+1] == 0:
            add_result(1, A[i])
            A[i] = 0
        else: 
            if min_val != A[i]:
                add_result(1, A[i] - min_val)
                    
            add_result(3, min_val)
            
            A[i] = 0
            A[i+1] -= min_val
            A[i+2] -= min_val


print(result)
    