import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

li = [[deque(), deque()] for _ in range(N+1)] ## fix, another

li[1][0].extend(list(range(1, N+1)))

target = N//2 + 1

now = 1
flag = False

def query_and_answer(li):
    str_li = list(map(str, li))
    
    print(f"? {' '.join(str_li)}")
    sys.stdout.flush()
    
    l, r, h = map(int, input().split())
    
    return l, r, h
    

for _ in range(10000):
    fix, another = li[now]
    
    if now < target:
        if len(fix) < N - now + 1:
            another.rotate(1)
            query = list(fix) + list(another)
            
            l, r, h = query_and_answer(query)
            
            if h == now:
                length_fix = len(fix)
                
                for _ in range(r-length_fix):
                    fix.append(another.popleft())
            else:
                li[h][0] = deque(query[l-1: r])
                li[h][1] = deque(query[:l-1] + query[r:])
                now = h
        else:
            fix.rotate(1)
            query = list(fix) + list(another)
            
            l, r, h = query_and_answer(query)
            
            if h != now:
                li[h][0] = deque(query[l-1: r])
                li[h][1] = deque(query[:l-1] + query[r:])
                now = h
                
    elif now > target:
        another.rotate(1)
        query = list(fix) + list(another)
        
        l, r, h = query_and_answer(query)
        
        if h == now:
            length_fix = len(fix)
            
            for _ in range(r-length_fix):
                fix.append(another.popleft())
        else:
            li[h][0] = deque(query[l-1: r])
            li[h][1] = deque(query[:l-1] + query[r:])
            now = h
        
    else:
        if len(fix) < N - now + 1:
            another.rotate(1)
            query = list(fix) + list(another)
            
            l, r, h = query_and_answer(query)
            
            if h == now:
                length_fix = len(fix)
                
                for _ in range(r-length_fix):
                    fix.append(another.popleft())
            else:
                li[h][0] = deque(query[l-1: r])
                li[h][1] = deque(query[:l-1] + query[r:])
                now = h
        else:
            for _ in range(len(fix)):
                val = fix.pop()
                
                for _ in range(len(another)):
                    query = list(fix) + list(another) + [val]
                    
                    l, r, h = query_and_answer(query)
                    
                    if l == 1 and h == now + 1:
                        flag = True
                        break
                    
                    another.rotate(1)
                
                if flag:
                    print(f"! {val}")
                    break
                
                fix.appendleft(val)
            
            if flag:
                break
