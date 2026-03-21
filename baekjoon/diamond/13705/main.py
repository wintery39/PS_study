import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

input = sys.stdin.readline

PI = Decimal('3.1415926535897932384626433832795028841971')
getcontext().prec = 64
    
def sin(x):
    if x >= 2*PI:
        return sin(x%(2*PI))
    if x > 1:
        return 2 * sin(x/2) * cos(x/2)
        
    ans = Decimal(x)
    frac = 1
    
    for i in range(1, 200):
        frac *= - (2*i) * (2*i+1)
        ans += x**(2*i+1) / frac
    
    return ans
    
def cos(x):
    if x >= 2*PI:
        return cos(x%(2*PI))
    if x > 1:
        return cos(x/2)**2 - sin(x/2)**2

    ans = Decimal(1)
    frac = 1
    
    for i in range(1, 200):
        frac *= - (2*i-1) * (2*i)
        ans += x**(2*i) / frac
    
    return ans

A, B, C = map(Decimal, input().split())

def is_bigger(num):
    return A*num+B*sin(num) >= C

def floor_at(num, k=6):
    return (((num*(10**k))//1)/(10**k))

min_num = Decimal(floor_at(C/A)-1)
max_num = Decimal(floor_at(C/A)+1)

def get_num(min_num, max_num):
    if min_num >= max_num:
        return min_num
    
    mid_num = floor_at((min_num + max_num)/2)
    
    if is_bigger(mid_num):
        return get_num(min_num, mid_num)
    else:
        k = mid_num+Decimal("0.000001")
        if is_bigger(k):
            return mid_num
        else:
            return get_num(k, max_num)

num = get_num(min_num, max_num)+Decimal("0.000001")


str_d = '0.00000'
d = 6
for _ in range(10):
    num -= Decimal(str_d+'1')
    str_d += '0'
    d += 1
    
    num += Decimal(str_d+'4')
    
    for i in range(4, 6):
        if A*num + B*sin(num) > C:
            break
        
        num += Decimal(str_d+'1')
    
    if num*(10**d)%10 != 5:
        break
    
print(num.quantize(Decimal('0.000000'), rounding=ROUND_HALF_UP))