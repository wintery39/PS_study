import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

li = map(int, input().split())

target = N
result_li = []

deq = deque(li)



while deq and len(result_li) <= N*N:
    if deq[-1] == target:
        target -= 1
        deq.pop()
        continue
    
    if len(deq) % 2 == 0 and deq[-2] == target:
        temp = deq.pop()
        result_li.append(len(deq) - 1)
        deq.rotate(2)
        deq.append(temp)
    else:    
        result_li.append(len(deq) - 1)
        deq.rotate(2)
    
    
if len(result_li) > N*N:
    print("NO")
else:
    print("YES")
    print(len(result_li))
    
    for i in result_li:
        print(i, end=" ")
        

