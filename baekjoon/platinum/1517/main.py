import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

cnt = 0
sorted_li = []
segement_tree = [0 for _ in range(N*4+2)]

for idx, num in enumerate(nums):
  sorted_li.append((idx, num))


sorted_li.sort(key=lambda x: x[1])

def updateTree(start, end, key, now_idx):
  segement_tree[now_idx] += 1
  
  if start + 1 == end:
    return

  mid = (start+end) // 2

  if key < mid:
    updateTree(start, mid, key, now_idx*2)
  else:
    updateTree(mid, end, key, now_idx*2+1)

def findTree(start, end, key, now_idx):
  if end <= key:
    return segement_tree[now_idx]
  
  mid = (start+end) // 2
  result = findTree(start, mid, key, now_idx*2)

  if mid < key :
    result += findTree(mid, end, key, now_idx*2+1)
  
  
  return result


for idx, _ in sorted_li:
  cnt += idx
  cnt -= findTree(0, N, idx, 1)
  updateTree(0, N, idx, 1)


print(cnt)


