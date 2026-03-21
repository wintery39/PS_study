import sys

input = sys.stdin.readline

N = int(input())

results = [0 for _ in range(10)]

divide_num = 10
    
while True:
    Q, R = N // divide_num, N % divide_num
    
    before = divide_num // 10
    
    for i in range(10):
        results[i] += Q*(before)
    
    for i in range(R//before):
        results[i] += before
    
    
    results[R//before] += R%before + 1
    
    results[0] -= before
    
    if Q == 0:
        break
        
    divide_num *= 10


for num in results:
    print(num, end=" ") 