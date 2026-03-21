import sys

input = sys.stdin.readline

N, K = map(int, input().split())

ramen = -1
AC_li = []

for _ in range(K):
    C, A = map(int, input().split())
    
    AC_li.append((A, C))
    
AC_li.sort(key=lambda x: -x[0]/(x[1]//2+1))

result = 0

for A, C in AC_li:
    ramen += C // 2 + 1
    
    if C%2==0:
        first = (ramen+1)*2
        second = (ramen)*2
        result += ((first + second) // 2) * A
    else:
        result += (ramen+1) * 2 * A

print(result)