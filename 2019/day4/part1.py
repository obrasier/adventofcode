from collections import Counter

start = 123257
finish = 647015
total_found = 0

def has_adjacent(digits, part):
  c = Counter(digits)
  if part == 1:
    if c.most_common(1)[0][1] >= 2:
      return True
  else:
    if 2 in c.values():
      return True    
  return False

def satisfies_critera(num, part):
  digits = list(map(int, str(num)))
  if sorted(digits) != digits:
    return False
  adj = has_adjacent(digits, part)
  if adj:
    return True
  return False


def run(part):
  total_found = 0
  for n in range(start, finish+1):
    if satisfies_critera(n, part):
      total_found += 1
  print(total_found)

run(part=1)
run(part=2)

