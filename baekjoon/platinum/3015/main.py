import sys

input = sys.stdin.readline

N = int(input())

li = []
li_len = 0
result = 0

def getBiggerIndex(start, end, target_value):
    if (start>end):
        return 0
    
    mid = (start + end) // 2
    
    if((li[mid] > target_value) and ((mid+1) == li_len or li[mid+1] <= target_value)):
        return mid
    elif(li[mid] > target_value):
        return getBiggerIndex(mid+1, end, target_value)
    else:
        return getBiggerIndex(start, mid-1, target_value)
        
def getBiggerOrSameIndex(start, end, target_value):
    if (start>end):
        return -1
    
    mid = (start + end) // 2
    
    if((li[mid] >= target_value) and ((mid+1) == li_len or li[mid+1] < target_value)):
        return mid
    elif(li[mid] >= target_value):
        return getBiggerOrSameIndex(mid+1, end, target_value)
    else:
        return getBiggerOrSameIndex(start, mid-1, target_value)


for _ in range(N):
    num = int(input())
    
    if(li_len>0):
        temp = getBiggerIndex(0, li_len-1, num)
        result += (li_len-temp)
        li_len = getBiggerOrSameIndex(0, li_len-1, num) + 1
        
    if(li_len == len(li)):
        li.append(num)
    else:
        li[li_len] = num
    
    li_len += 1
    
print(result)