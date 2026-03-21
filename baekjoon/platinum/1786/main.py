import sys

input = sys.stdin.readline

T = input()[:-1]
P = input()[:-1]

pattern_li = [-1 for _ in P]

idx = 0
for p in range(1, len(P)):
  while True:
    if P[idx] == P[p]:
      pattern_li[p] = idx
      break
    if idx == 0:
      idx = -1
      break
    idx = pattern_li[idx-1] + 1
  
  idx += 1

target_idx = 0
pattern_idx = 0

result = []


while target_idx < len(T):
  if T[target_idx] == P[pattern_idx]:
    target_idx += 1
    pattern_idx += 1

    if pattern_idx == len(P):
      result.append(target_idx-pattern_idx + 1)
      pattern_idx = pattern_li[pattern_idx-1] + 1
  elif pattern_idx == 0:
    target_idx += 1
  else:
    pattern_idx = pattern_li[pattern_idx-1] + 1


print(len(result))
print(" ".join(map(str, result)))