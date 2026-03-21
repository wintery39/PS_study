import sys

input = sys.stdin.readline

_ = input()

num_li = list(map(int, input().split()))

increase_li = []
idx_li = [[] for _ in range(len(num_li))]

def insert_li(num, li, num_li_idx):
  start = 0
  end = len(li) -1
  
  while True:
    if start>end:
      if start== len(li):
        li.append(num)
      else:
        li[start] = num
      idx_li[start].append(num_li_idx)
      break

    idx = max((start + end) // 2, 0)
  
    if li[idx] == num:
      break
    elif li[idx] > num:
      end = idx - 1
    elif li[idx] < num:
      start = idx+1

  return li
  

for idx, i in enumerate(num_li):
  increase_li = insert_li(i, increase_li, idx)



result = [num_li[idx_li[len(increase_li)-1][0]]]

for idx in range(len(increase_li) - 2, -1, -1):
  for i in idx_li[idx]:
    if result[-1] > num_li[i]:
      result.append(num_li[i])
      break

result.reverse()
print(len(increase_li))
print(" ".join(map(str, result)))